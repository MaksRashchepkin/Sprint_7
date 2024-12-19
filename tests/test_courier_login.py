import allure
import pytest
import requests

from base_metods.base_metods import create_courier_for_test
from data import URL, URL_COURIER, URL_LOGIN


class TestUserLogin:

    @allure.description(
        'Проверяем, что курьер может авторизоваться'
    )
    def test_courier_authorization_success(self):
        payload=create_courier_for_test()
        response = requests.post(f'{URL}{URL_COURIER}', payload)
        response = requests.post(f'{URL}{URL_LOGIN}', payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.description(
        'Проверяем, что для авторизации нужно передать все обязательные поля'
    )
    def test_fill_all_mandatory_fields_to_login(self):
        payload=create_courier_for_test()
        values = list(payload.values())
        response = requests.post(f'{URL}{URL_COURIER}', payload)
        payload = {
        "login": values[0],
        "password": ""
        }

        response = requests.post(f'{URL}/courier/login', payload)

        assert response.status_code == 400 and response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.description(
        'Проверяем, что система вернет ошибку, если неправильно указать логин или пароль'
    )
    def test_return_error_if_wrong_credentials(self):
        payload=create_courier_for_test()
        values = list(payload.values())
        response = requests.post(f'{URL}{URL_COURIER}', payload)
        payload = {
        "login": values[0],
        "password": values[2]
        }

        response = requests.post(f'{URL}{URL_LOGIN}', payload)

        assert response.status_code == 404 and response.text == '{"code":404,"message":"Учетная запись не найдена"}'

    @allure.description(
        'Проверяем, что если какого-то поля нет, запрос возвращает ошибку'
    )
    def test_error_with_empty_field(self):
        payload = create_courier_for_test()
        values = list(payload.values())
        response = requests.post(f'{URL}{URL_COURIER}', payload)
        payload = {
            "login": '',
            "password": values[1]
        }

        response = requests.post(f'{URL}{URL_LOGIN}', payload)

        assert response.status_code == 400 and response.text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.description(
        'Проверяем, что успешный запрос возвращает id'
    )
    def test_return_id_if_authorization_success(self):
        payload=create_courier_for_test()
        response = requests.post(f'{URL}{URL_COURIER}', payload)
        response = requests.post(f'{URL}{URL_LOGIN}', payload)

        assert "id" in response.text
