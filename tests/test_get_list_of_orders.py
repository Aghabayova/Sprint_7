import allure

from helpers import *

from data import APILinks


class TestGetOrdersList:
    @allure.title('Return list of orders')
    def test_get_list_of_orders(self):
        r = requests.get(APILinks.MAIN_URL + APILinks.ORDERS_URL)
        orders_list = r.json()["orders"]
        assert r.status_code == 200 and type(orders_list) == list