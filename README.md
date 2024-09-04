# <h><center> Project: Yandex Scooter API test</h>


### prepared by Samira Aghabayova


## Test Coverage:

## 1. Courier Creation

**test_create_courier - Verify a courier can be created successfully.**

**test_create_duplicate_courier - Verify creating a courier with an existing login fails.**

**test_create_courier_without_credentials - Verify the system returns an error if required fields are missing.** 


## 2. Courier Login

**test_courier_login - Verify a courier can login with valid credentials.**

**test_courier_login_without_credentials - Verify login fails if required fields are missing.**

**test_courier_login_non_existent - Verify login fails for a courier that does not exist.**


## 3. Order Creation

**test_create_order - Order Creation with one of the scooter Colors**

## 4. Order list

**test_get_list_of_orders - Verify that the list of orders is returned**



## Project Launch: 

1. Install pytest using pip:
```
    pip install pytest
```
2. Install selenium using pip:

```
   pip install selenium
```
3. Install allure using homebrew:

```
   brew install allure
```
4. Run the Tests with pytest:

```
   pytest -v
```
## Comands to obtain the report


1. Install pytest using pip:
```
pytest --alluredir=allure_results
```
2. Install selenium using pip:

```
 allure serve allure_results
```