import requests

def test_home():
    response = requests.get("http://localhost")
    assert response.status_code == 200
