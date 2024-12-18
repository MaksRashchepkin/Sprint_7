import allure
import requests
from data import Endpoint, Message
from conftest import create_courier
from helpers import *

class TestAuthCourier:
    @allure.step('Авторизация курьера')
    def test_auth_courier(self, create_courier):
        login_pass = create_courier
        response = requests.post(Endpoint.login_courier, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        assert response.status_code == 200
        assert Message.login_courier in response.text

    @allure.step('Авторизация курьера без логина')
    def test_auth_courier_without_login(self, create_courier):
        login_pass = create_courier
        response = requests.post(Endpoint.login_courier, data={
            'login': '',
            'password': login_pass[1]
        })
        assert response.status_code == 400
        assert Message.login_courier_without_data == response.text

    @allure.step('Авторизация курьера без пароля')
    def test_auth_courier_without_password(self, create_courier):
        login_pass = create_courier
        response = requests.post(Endpoint.login_courier, data={
            'login': login_pass[0],
            'password': ''
        })
        assert response.status_code == 400
        assert Message.login_courier_without_data == response.text

    @allure.step('Авторизация несуществующего курьера')
    def test_auth_not_existing_courier(self):
        response = requests.post(Endpoint.login_courier, data={
            'login': 'Ivan',
            'password': 'abc654321'
        })
        assert response.status_code == 404
        assert Message.login_not_existing_courier == response.text
