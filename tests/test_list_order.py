import allure
import requests
from data import Endpoint, Message

class TestListOrder:
    @allure.step('Получить список заказов')
    def test_list_order(self):
        response = requests.get(Endpoint.order_list)
        assert response.status_code == 200
        assert Message.list_orders in response.text
