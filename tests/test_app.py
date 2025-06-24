import pytest
from app import app, process_line, group_pins, create_pin


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


def test_process_line():
    mintrest_data = ['1234\n','Carla\n', 'This is me\n', 'Image\n']
    assert process_line(mintrest_data) == ['1234', 'Carla', 'This is me', 'Image']


def test_group_pins():
    pins = ['1234', 'Carla', 'This is me', 'Image', '5678', 'Buongiorno', 'This is also me', 'Image2']
    assert group_pins(pins) == [['1234', 'Carla', 'This is me', 'Image'], ['5678', 'Buongiorno', 'This is also me', 'Image2']]


def test_create_pin():
    assert create_pin('1234', 'Carla', 'This is me', 'Image') == {
                                                                    'timestamp': '1234',
                                                                    'date': '01 January 1970',
                                                                    'title': 'Carla',
                                                                    'description': 'This is me',
                                                                    'image': 'Image'
                                                                }
                                                    