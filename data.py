class APILinks:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    LOGIN_URL = 'api/v1/courier/login'
    COURIER_URL = 'api/v1/courier/'
    ORDERS_URL = 'api/v1/orders'


class CourierData:
    only_password = {"password": "Password"}
    empty_password = {"login": "Login", "password": ""}
    empty_login = {"login": "", "password": "Password"}
    without_login = {"password": "Password", "firstName": 'Name'}
    without_password = {"login": "Login", "firstName": "Name"}
    empty_login_courier = {"login": "", "password": "Password", "firstName": "Name"}
    empty_password_courier = {"login": "Login", "password": "", "firstName": "Name"}


class OrderData:
    order_data = {
        "firstName": "Вильям",
        "lastName": "Шекспир",
        "address": "ул. Европейская, д.1",
        "metroStation": 4,
        "phone": "+7 654 123 45 67",
        "rentTime": 4,
        "deliveryDate": "2024-12-20",
        "comment": "оставить у подъезда"
    }


class StatusMessage:
    text_login_400 = "Недостаточно данных для входа"
    text_login_404 = "Учетная запись не найдена"
    text_create_201 = '{"ok":true}'
    text_create_409 = "Этот логин уже используется. Попробуйте другой."
    text_create_400 = "Недостаточно данных для создания учетной записи"
