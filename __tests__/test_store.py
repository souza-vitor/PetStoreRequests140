import pytest 
import requests
import json

order_id = 173549300
pet_id = 173754901
order_quantity = 1
order_ship_date = "2025-06-28T13:49:18.620+0000"
order_status = "placed"
complete = True

url="https://petstore.swagger.io/v2/store/order"
headers={'Content-Type': 'application/json'}


def test_order_post():
    order=open('./fixtures/json/order1.json')       
    data=json.loads(order.read())

    response = requests.post(                   
        url=url,                                
        headers=headers,                        
        data=json.dumps(data),                  
        timeout=5                               
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == order_id
    assert response_body['shipDate'] == order_ship_date
    assert response_body['complete'] == True


def test_order_get():

    response = requests.get(
        url=f"{url}/{order_id}",
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == order_id
    assert response_body['petId'] == pet_id
    assert response_body['shipDate'] == order_ship_date


def test_order_delete():

    response = requests.delete(
        url=f"{url}/{order_id}",
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(order_id)