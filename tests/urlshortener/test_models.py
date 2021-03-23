from django.conf import settings
import pytest
from apps.urlshortener.models import URL
from apps.urlshortener.helpers import Base62


@pytest.mark.django_db
def test_base62_encoded_id():
    for i in range(100):
        URL.objects.create(long_url=f'http://example{i}.com')

    obj = URL.objects.create(long_url='https://www.youtube.com/watch?v=WY5kGvKXUqE&list=RDWY5kGvKXUqE')
    assert URL.objects.count() == 101
    assert obj.slug == Base62.encode(101 + settings.URL_SHORTENER_SALT)
