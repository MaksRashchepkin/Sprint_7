import allure
import requests
from data import Urls

class OrderMethods:
    @allure.step("Создание заказа с данными")
    def create_order(self, payload):
        return requests.post(Urls.CREATE_ORDER_URL, json=payload)

    @allure.step("Получение списка всех заказов")
    def get_orders(self):
        response = requests.get(Urls.GET_ORDERS_URL)
        return response

    @allure.step("Принимаем заказ с ID заказа и курьера")
    def accept_order(self, order_id, courier_id):
        if courier_id is not None:
            url = f'{Urls.ACCEPT_ORDER_URL}{order_id}?courierId={courier_id}'
        else:
            url = f'{Urls.ACCEPT_ORDER_URL}{order_id}?courierId='

        response = requests.put(url)
        return response

    @allure.step("Получение заказа по ID")
    def get_order_by_id(self, order_id):
        return requests.get(f'{Urls.GET_ORDERS_URL}/track?t={order_id}')
