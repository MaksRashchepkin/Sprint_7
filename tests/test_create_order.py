import allure
import requests
import pytest
from data import Endpoint, Message, User

class TestCreateOrder:
    @allure.step('Создать заказ с разными цветами самоката')
    @pytest.mark.parametrize('colour', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, colour):
        payload = User.user
        payload['colour'] = colour
        response = requests.post(Endpoint.create_order, json=payload)
        assert response.status_code == 201
        assert Message.create_order in response.text
