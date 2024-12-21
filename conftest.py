import pytest
from methods.courier_methods import CourierMethods

@pytest.fixture
def courier_data():
    courier_methods = CourierMethods()
    data = courier_methods.generate_courier_data()
    yield data
    courier_methods.delete_courier(data['login'], data['password'])
