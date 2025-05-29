import requests
import responses

@responses.activate
def test_home():
    responses.add(responses.GET, "http://localhost", json={}, status=200)
    response = requests.get("http://localhost")
    assert response.status_code == 200
