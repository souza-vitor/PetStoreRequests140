import pytest 
import requests
import json

from utils.utils import ler_csv

user_id = 173549010
username = "mirosantana99"
user_first_name = "Miro"
user_last_name = "Santana"
user_email = "miro_santana@starlink.com"
user_password = "plaintext2!"
user_phone = "5521987654321"
user_status = 1

url="https://petstore.swagger.io/v2/user"
headers={'Content-Type': 'application/json'}


def test_user_post():
    user=open("./fixtures/json/user1.json")
    data=json.loads(user.read())

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()


    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)


def test_user_get():
    response = requests.get(
        url=f'{url}/{username}',
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == user_id
    assert response_body['username'] == username
    assert response_body['email'] == user_email
    #assert response_body['userStatus'] == user_status


def test_user_put():
    user=open("./fixtures/json/user2.json")
    data=json.loads(user.read())


    response = requests.put(
        url=f'{url}/{username}',
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)

def test_user_delete():

    response = requests.delete(
        url=f"{url}/{username}",
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(username)