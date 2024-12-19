import json

import allure
import pytest
import requests

from data import URL, URL_ORDER, colors, order


class TestCreateOrder:

    @allure.description(
        'Проверяем, что заказ можно создать с любым цветом или без него'
    )
    @pytest.mark.parametrize('color', colors)

    def test_set_color(self, color):
        json_string = json.dumps(order)
        response = requests.post(f'{URL}{URL_ORDER}', json_string)
        assert response.status_code == 201 and 'track' in response.text