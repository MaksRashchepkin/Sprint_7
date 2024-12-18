class Endpoint:
    scooter_url = 'https://qa-scooter.praktikum-services.ru'
    # POST
    create_courier = f'{scooter_url}/api/v1/courier'
    login_courier = f'{scooter_url}/api/v1/courier/login'
    create_order = f'{scooter_url}/api/v1/orders'
    # GET
    order_list = f'{scooter_url}/api/v1/orders'
    get_order_track = f'{scooter_url}/api/v1/orders/track'
    # DELETE
    delete_courier = f'{scooter_url}/api/v1/courier/'

class Message:
    create_courier = '{"ok": true}'
    create_existing_courier = '{"code": 409, "message": "Этот логин уже используется"}'
    create_courier_without_login = '{"code": 400, "message": "Недостаточно данных для создания учетной записи"}'
    login_courier = 'id'
    login_courier_without_data = '{"code": 400, "message":  "Недостаточно данных для входа"}'
    login_not_existing_courier = '{"code": 404, "message": "Учетная запись не найдена"}'
    create_order = 'track'
    list_orders = 'orders'
    delete_courier = '{"ok": true}'
    delete_courier_without_id = '{"code": 400, "message":  "Недостаточно данных для удаления курьера"}'
    delete_not_existing_courier = '{"code": 404, "message": "Курьера с таким id нет"}'

class User:
    user = {
        'firstname': 'Maksim',
        'lastname': 'Rashchepkin',
        'address': 'Moscow',
        'metrostation': 7,
        'phone': '+79143295156',
        'renttime': '3',
        'deliverydate': '2024-12-19',
        'comment': '',
        'color': []
    }
