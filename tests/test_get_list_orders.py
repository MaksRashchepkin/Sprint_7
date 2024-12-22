import allure
from methods.order_methods import OrderMethods

@allure.epic("Тестирование на получение списка заказов")
class TestGetOrders:
    order_methods = OrderMethods()

    @allure.title("Тест на получение списка заказов")
    @allure.description("Проверка, что запрос на получение списка заказов возвращает статус 200 и корректную структуру ответа.")
    def test_get_orders(self):
        response = self.order_methods.get_orders()

        assert response.status_code == 200

        response_json = response.json()
        assert "orders" in response_json

        assert isinstance(response_json["orders"], list)
