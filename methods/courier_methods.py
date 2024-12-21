import random
import string
import allure
import requests
from data import Urls

class CourierMethods:
    @allure.step("Генерация данных для регистрации курьера")
    def generate_courier_data(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            'login': f'{login}',
            'password': f'{password}',
            'firstName': f'{first_name}'
        }
        return payload

    @allure.step("Регистрация курьера")
    def create_courier(self, payload):
        return requests.post(Urls.courier_registration_url, json=payload)

    @allure.step("Логинимся как курьер")
    def login_courier(self, payload):
        return requests.post(Urls.courier_login_url, json=payload)

    @allure.step("Получение ID курьера")
    def get_courier_id(self, login, password):
        login_payload = {
            "login": login,
            "password": password
                        }
        login_response = self.login_courier(login_payload)
        return login_response.json().get("id")

    @allure.step("Удаление курьера через логин и пароль")
    def delete_courier(self, login, password):
        courier_id = self.get_courier_id(login, password)
        response = requests.delete(f'{Urls.courier_registration_url}/{courier_id}')
        return response

    @allure.step("Удаление курьера с ID")
    def delete_courier_with_id(self, courier_id):
        response = requests.delete(f'{Urls.courier_registration_url}/{courier_id}')
        return response
