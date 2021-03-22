import pytest 


def test_root_endpoint(client):
    response = client.get('/')
    assert response.json() == {'message': 'API is up and running.'}


@pytest.mark.freeze_time('2021-02-01 07:15:30')
def test_server_time(client):
    response = client.get('/server_time')
    assert response.json() == {'server_time': '2021-02-01T07:15:30Z'}
