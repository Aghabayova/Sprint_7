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
        response = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Login fails if required fields are missing')
    @pytest.mark.parametrize('courier_data', (
            CourierData.empty_login,
            CourierData.empty_password,
            CourierData.only_password))
    def test_courier_login_without_credentials(self, courier_data):
        payload = courier_data
        response = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=payload)

        assert response.status_code == 400 and response.json()['message'] == StatusMessage.TEXT_LOGIN_400

    @allure.title('Login fails for a courier that does not exist.')
    def test_courier_login_non_existent(self, create_and_delete_courier):
        payload = {"login": create_and_delete_courier[1][1],
                   "password": create_and_delete_courier[1][0]}
        response = requests.post(APILinks.MAIN_URL + APILinks.LOGIN_URL, data=payload)
        assert response.status_code == 404 and response.json()['message'] == StatusMessage.TEXT_LOGIN_404
