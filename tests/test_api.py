import requests

def test_home():
    response = requests.get("http://localhost")
    assert response.status_code == 200

def test_api():
    response = requests.get("http://localhost/api/")
    assert response.status_code == 200
