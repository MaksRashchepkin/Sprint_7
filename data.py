
class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_LOGIN_URL = f'{BASE_URL}/api/v1/courier/login'
    COURIER_REGISTRATION_URL = f'{BASE_URL}/api/v1/courier'
    CREATE_ORDER_URL= f'{BASE_URL}/api/v1/orders'
    CANCEL_ORDER_URL= f'{BASE_URL}/api/v1/orders/cancel'
    GET_ORDERS_URL = f'{BASE_URL}/api/v1/orders'
    ACCEPT_ORDER_URL = f'{BASE_URL}/api/v1/orders/accept/'

class OrderData:
    ORDER_DATA_1= {
            "first_name": "Maksim",
            "last_name": "Rashchepkin",
            "address": "Kirova, 25",
            "metro_station": 5,
            "phone": "+79143295157",
            "rent_time": 2,
            "delivery_date": "2024-12-25",
            "comment": "Zvonit zaranee",
            "color": ["GREY"],
            "expected_status": 201
    }
