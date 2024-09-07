import requests
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_new_courier_and_return_login_password():
    # create a list so that the method can return it.
    login_pass = []

    # generate the courier's login, password, and name.
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # assemble the request body.
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # send a request to register a courier and save the response in the response variable.
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # if the registration is successful (response code 201), add the courier's login and password to the list.
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    # return the list and the response.
    return response, login_pass


# generate a password.
def generate_login_pass():
    login_pass = []
    for i in range(3):
        random_login_pass_data = generate_random_string(10)
        login_pass.append(random_login_pass_data)
    return login_pass