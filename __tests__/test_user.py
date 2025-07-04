import pytest 
import requests
import json
import time


from utils.utils import ler_csv

user_id = 173549111
username = "mirosantana99"
user_first_name = "Miro"
user_last_name = "Santana"
user_email = "miro_santana@starlink.com"
user_password = "plaintext2!"
user_phone = "5521987654321"
user_status = 1

url="https://petstore.swagger.io/v2/user"
headers={'Content-Type': 'application/json'}


@pytest.mark.order(1)
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
    time.sleep(4)


@pytest.mark.order(2)
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
    time.sleep(2)


@pytest.mark.order(3)
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
    time.sleep(2)


@pytest.mark.order(4)
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
    #time.sleep(4)


@pytest.mark.order(5)
@pytest.mark.parametrize('user_id,username,user_first_name,user_last_name,user_email,user_password,user_phone,user_status',
                         ler_csv('./fixtures/csv/users.csv'))
def test_user_post_dinamico(user_id,username,user_first_name,user_last_name,user_email,user_password,user_phone,user_status):
    user = {}
    user['id'] = int(user_id)
    user['username'] = username
    user['firstName'] = user_first_name
    user['lastName'] = user_last_name
    user['email'] = user_email
    user['password'] = user_password
    user['phone'] = user_phone
    user['userStatus'] = int(user_status)

    user = json.dumps(obj=user, indent=4)

    response = requests.post(
        url=url,
        headers=headers,
        data=user,
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)
    #time.sleep(4)


@pytest.mark.order(6)
@pytest.mark.parametrize('user_id,username',
                         ler_csv('./fixtures/csv/users_delete.csv'))
def test_user_delete_dinamico(user_id,username):
    response = requests.delete(
        url=f"{url}/{username}",
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(username)
    time.sleep(4)