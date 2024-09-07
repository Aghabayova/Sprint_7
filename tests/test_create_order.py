import pytest
import allure
import json
from helpers import *
from data import APILinks, OrderData


class TestCreateOrder:
    @allure.title('Order Creation with one of the scooter Colors')
    @pytest.mark.parametrize('color', (["BLACK"], ["GREY"], ["BLACK", "GREY"], []))
    def test_create_order(self, color):
        OrderData.order_data["color"] = [color]
        payload = json.dumps(OrderData.order_data)
        response = requests.post(APILinks.MAIN_URL + APILinks.ORDERS_URL, data=payload)
        assert response.status_code == 201 and 'track' in response.text