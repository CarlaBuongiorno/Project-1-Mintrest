import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200


def test_newpost_route(client):
    response = client.get('/newpost/')
    assert response.status_code == 200
