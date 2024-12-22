Tests for API Яндекс Самокат

Сценарии, покрытые тестами:
Тестирование на создание курьера - test_create_courier.py:
test_create_courier - Тест на создание нового курьера
test_create_duplicate_courier - Тест на создание дублирующего курьера
test_create_courier_missing_fields - Тест на создание курьера без обязательных полей
test_create_courier_with_existing_login - Тест на создание курьера с уже существующим логином

Тестирование на создание заказа - test_create_order.py:
test_create_order - Тест на создание заказа

Тестирование на удаление курьера - test_delete_courier.py:
test_delete_courier_success - Тест на успешное удаление курьера
test_delete_courier_no_id - Тест на удаление курьера без указания ID
test_delete_courier_nonexistent_id - Тест на удаление курьера с несуществующим ID

Тестирование на получение списка заказов - test_get_list_orders.py
test_get_orders - Тест на получение списка заказов

Тестирование на получение заказа по номеру - test_get_order.py
test_get_order_success - Тест на успешное получение заказа по ID
test_get_order_missing_order_id - Тест на получение заказа без указания ID
test_get_order_invalid_order_id - Тест на получение заказа с невалидным ID

Тестирование на логин курьеров - test_login_courier.py
test_login_courier_with_invalid_data - Тест на логин с некорректными данными
test_login_courier_success - Тест на успешный логин курьера
test_login_nonexistent_courier - Тест на вход несуществующего курьера

Тестирование на принятие заказов - test_order_acceptance.py
test_accept_order_success - Тест на успешное принятие заказа
test_accept_order_missing_courier_id - Тест на принятие заказа без указания ID курьера
test_accept_order_invalid_courier_id - Тест на принятие заказа с невалидным ID курьера
test_accept_order_missing_order_id - Тест на принятие заказа без указания ID заказа
test_accept_order_invalid_order_id - Тест на принятие заказа с невалидным ID заказа

Для запуска тестирования:
Установить зависимости - pip3 install -r requirements.txt
Запустить все тесты из директории tests - pytest tests --alluredir=allure_results
Посмотреть отчет - allure serve allure_results
