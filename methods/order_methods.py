import allure
import requests
from data import Urls

class OrderMethods:
    @allure.step("Создание заказа с данными")
    def create_order(self, payload):
        return requests.post(Urls.create_order_url, json=payload)

    @allure.step("Получение списка всех заказов")
    def get_orders(self):
        response = requests.get(Urls.get_orders_url)
        return response

    @allure.step("Получение зазказа по ID")
    def get_order_by_id(self, order_id):
        return requests.get(f'{Urls.get_orders_url}/track?t={order_id}')
