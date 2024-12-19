import allure
import requests
from data import Endpoint, Message
from helpers import *

class TestDeleteCourier:
    @allure.step('Удалить курьера')
    def test_delete_courier(self):
        login_pass = register_new_courier_and_return_password()
        response = requests.post(Endpoint.login_courier, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        courier_id = response.json()['id']
        response_delete = requests.delete(f'{Endpoint.delete_courier}{courier_id}')
        assert response_delete.status_code == 200
        assert Message.delete_courier == response_delete.text


    @allure.step('Удалить несуществующего курьера')
    def test_delete_not_existing_courier(self):
        login_pass = register_new_courier_and_return_password()
        response = requests.post(Endpoint.login_courier, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        courier_id = 123456
        response_delete = requests.delete(f'{Endpoint.delete_courier}{courier_id}')
        assert response_delete.status_code == 404
        assert Message.delete_not_existing_courier == response_delete.text


    @allure.step('Удалить курьера без id')
    def test_delete_courier_without_id(self):
        response = requests.delete(Endpoint.delete_courier)
        assert response.status_code == 400
        assert Message.delete_courier_without_id == response.text
