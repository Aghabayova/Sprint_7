import pytest
import allure
from helpers import *
from conftest import create_and_delete_courier
from data import APILinks, CourierData, StatusMessage


class TestLoginCourier:
    @allure.title('A courier can login with valid credentials. ')
    def test_courier_login(self, create_and_delete_courier):
        payload = {"login": create_and_delete_courier[1][0],
                   "password": create_and_delete_courier[1][1]}
        r = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=payload)
        assert r.status_code == 200 and 'id' in r.json()

    @allure.title('Login fails if required fields are missing')
    @pytest.mark.parametrize('courier_data', (
            CourierData.empty_login,
            CourierData.empty_password,
            CourierData.only_password))
    def test_courier_login_without_credentials(self, courier_data):
        payload = courier_data
        r = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=payload)

        assert r.status_code == 400 and r.json()['message'] == StatusMessage.text_login_400

    @allure.title('Login fails for a courier that does not exist.')
    def test_courier_login_non_existent(self, create_and_delete_courier):
        payload = {"login": create_and_delete_courier[1][1],
                   "password": create_and_delete_courier[1][0]}
        r = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=payload)
        assert r.status_code == 404 and r.json()['message'] == StatusMessage.text_login_404
