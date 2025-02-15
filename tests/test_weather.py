# tests/test_weather.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_weather_data(client):
    response = client.get('/weather/1')
    assert response.status_code == 200
    # Add more assertions to check the response data
