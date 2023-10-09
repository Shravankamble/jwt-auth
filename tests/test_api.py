import pytest, requests

# this tests are in development so the host is localhost not any other host 
ENDPOINT = "https://1ba2-183-87-183-181.ngrok-free.app/"

# this are the routes
routes = [
    "api/v1/jwt/dict",
    "api/v1/jwt/user"
]

def test_api_call_route_dict():
    payload = {
        "name": "shravan",
        "password": "48a71c7749bc70de07ae6910231458c3996eacb84c8cad9359def57248833c1d6392",
        "id": "9594ab3495921afc6e8b7485"
    }
    resp = requests.post(ENDPOINT + routes[0], json=payload)
    print(resp.text)
    assert resp.status_code == 200
    
def test_api_call_route_user():
    payload = {
        "email": "dummyuser@gmail.com",
        "password": "4745bd5d364f320e3473e7dd6f4f348fdac0bcc6"
    }
    resp = requests.post(ENDPOINT + routes[1], json=payload)
    print(resp.text)
    assert resp.status_code == 200
