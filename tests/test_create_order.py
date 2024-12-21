import allure
import pytest
from methods.order_methods import OrderMethods

@allure.epic("Тест на создание заказа")
class TestCreateOrder:
    order_methods = OrderMethods()
    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])

    @allure.title("Тест на создание заказа с разным цветом/без цвета")
    @allure.description("Проверка, что, когда создаёшь заказ: можно указать один из цветов — BLACK или GREY, можно указать оба цвета, можно совсем не указывать цвет, тело ответа содержит track.")
    def test_create_order(self, color):
        order_data = {
            "first_name": "Максим",
            "last_name": "Ращепкин",
            "address": "Кирова 21",
            "metro_station": 7,
            "phone": "+79143295157",
            "rent_time": 2,
            "delivery_date": "2024-12-25",
            "comment": "Позвонить за час",
            "color": color
        }

        response = self.order_methods.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json(), "Response does not contain 'track'"
