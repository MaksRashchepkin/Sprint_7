from base_metods.base_metods import create_courier_for_test
from data import URL, payload_first, payload_second, URL_COURIER, URL_LOGIN

import allure
import requests

class TestCouriers:

    @allure.description(
        'Проверка, курьера можно создать'
    )
    def test_correct_create_courier(self):
        payload=create_courier_for_test()
        response = requests.post(f'{URL}{URL_COURIER}', payload)
        response = requests.post(f'{URL}{URL_LOGIN}', payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.description(
        'Проверка, нельзя создать двух одинаковых курьеров'
    )
    def test_not_create_courier_with_2_identical_payload(self):
        payload = create_courier_for_test()
        response = requests.post(f'{URL}{URL_COURIER}', payload)

        response = requests.post(f'{URL}{URL_COURIER}', payload)

        assert response.status_code == 409 and response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.description(
        'Проверка, если создать пользователя с логином, который уже есть, возвращается ошибка.'
    )
    def test_not_create_courier_with_2_identical_payload(self):

        response = requests.post(f'{URL}{URL_COURIER}', payload_first)

        response = requests.post(f'{URL}{URL_COURIER}', payload_second)

        assert response.status_code == 409 and response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'


    @allure.description(
        'Проверка, чтобы создать курьера, нужно передать в ручку все обязательные поля'
    )
    def test_fill_all_needed_fields_to_set_courier(self):
        payload = create_courier_for_test()
        values = list(payload.values())
        response = requests.post(f'{URL}{URL_COURIER}', payload)

        payload = {
            "login": values[0],
            "password": "",
            "firstName": values[2]
        }

        response = requests.post(f'{URL}{URL_COURIER}', payload)
        assert response.status_code == 400

    @allure.description(
        'Проверка, запрос возвращает правильный код ответа'
    )
    def test_correct_code_create_courier(self):
        payload=create_courier_for_test()
        response = requests.post(f'{URL}{URL_COURIER}', payload)
        response = requests.post(f'{URL}{URL_LOGIN}', payload)
        assert response.status_code == 200


    @allure.description(
        'Проверка, успешный запрос возвращает {"ok":true}'
    )
    def test_request_return_correct_answer(self):
        payload = create_courier_for_test()
        response = requests.post(f'{URL}{URL_COURIER}', payload)

        assert response.status_code == 201 and response.text == '{"ok":true}'


    @allure.description(
        'Проверка, если одного из полей нет, запрос возвращает ошибку.'
    )
    def test_receive_error_if_mandatory_field_is_empty(self):
        payload = create_courier_for_test()
        values = list(payload.values())
        response = requests.post(f'{URL}{URL_COURIER}', payload)

        payload = {
            "login": "",
            "password": values[1],
            "firstName": values[2]
        }

        response = requests.post(f'{URL}{URL_COURIER}', payload)

        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
