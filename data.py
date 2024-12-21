
class Urls:
    base_url = 'https://qa-scooter.praktikum-services.ru'
    courier_login_url = f'{base_url}/api/v1/courier/login'
    courier_registration_url = f'{base_url}/api/v1/courier'
    create_order_url = f'{base_url}/api/v1/orders'
    get_orders_url = f'{base_url}/api/v1/orders'

class OrderData:
    order_data= {
            "first_name": "Максим",
            "last_name": "Ращепкин",
            "address": "Кирова 21",
            "metro_station": 7,
            "phone": "+79143295157",
            "rent_time": 2,
            "delivery_date": "2024-12-25",
            "comment": "Позвонить за час",
            "color": ["GREY"],
            "expected_status": 201
        }
