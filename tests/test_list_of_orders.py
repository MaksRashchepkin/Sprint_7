import pytest
import requests

import allure

from data import URL, orderEndpoints


class TestListOfOrders:

   @allure.description(
      'Получаем список заказов в теле ответа, отправляя различные данные'
   )
   @pytest.mark.parametrize('orderEndpoint', orderEndpoints)
   def test_get_list_of_orders(self, orderEndpoint):

      response = requests.get(f'{URL}/{orderEndpoint}')
      assert response.status_code == 200 and "orders" in response.text