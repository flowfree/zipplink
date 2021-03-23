from django.conf import settings
import pytest 
from apps.urlshortener.models import URL
from apps.urlshortener.helpers import Base62


@pytest.mark.django_db
def test_create_new_short_url(client):
    numrows = URL.objects.count()
    response = client.post('/urls', {'long_url': 'http://example.com'})

    assert URL.objects.count() == numrows+1

    obj = URL.objects.last()
    encoded = Base62.encode(obj.pk + settings.URL_SHORTENER_SALT)

    assert obj.long_url == 'http://example.com'
    assert obj.short_url == f'{settings.URL_SHORTENER_PREFIX}/{obj.slug}'


@pytest.mark.django_db
def test_add_existing_url(client):
    obj = URL.objects.create(long_url='http://example.com/a/b/c.html')
    numrows = URL.objects.count()

    response = client.post('/urls', {'long_url': 'http://example.com/a/b/c.html'})

    assert URL.objects.count() == numrows
    assert response.json()['long_url'] == 'http://example.com/a/b/c.html'
    assert response.json()['short_url'] == obj.short_url


@pytest.mark.django_db
def test_add_invalid_url(client):
    response = client.post('/urls', {'long_url': 'abcdef'})

    assert response.status_code == 400
    assert response.json() == {'long_url': ['Enter a valid URL.']}


@pytest.mark.django_db
def test_redirect_short_URL_to_original_URL(client):
    obj = URL.objects.create(long_url='https://www.youtube.com/watch?v=6FNHe3kf8_s')

    response = client.get(f'http://{obj.short_url}')

    assert response.status_code == 302
    assert response.url == 'https://www.youtube.com/watch?v=6FNHe3kf8_s'
