import requests


def test_status_code_ok():
    response = requests.get("https://httpbin.org/get", verify=False)
    assert response.status_code == 200

def test_json_response():
    response = requests.get("https://httpbin.org/get", verify=False)
    data = response.json()
    assert "url" in data
    assert data["url"] == "https://httpbin.org/get"

def test_post_request():
    payload = {"key": "value"}
    response = requests.post("https://httpbin.org/post", json=payload, verify=False)
    assert response.status_code == 201
    data = response.json()
    assert data["json"] == payload

def test_headers():
    headers = {"Custom-Header": "TestValue"}
    response = requests.get("https://httpbin.org/headers", headers=headers, verify=False)
    data = response.json()
    assert data["headers"]["Custom-Header"] == "TestValue"
