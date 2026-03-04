import requests
from data import BASE_URL, CREATE_COURIER_PATH
import allure
from helpers import register_new_courier, delete_courier

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Создание курьера с валидными данными")
    def test_create_courier_success(self):
        payload = register_new_courier()
        courier_id = requests.post(BASE_URL + "/api/v1/courier/login", data={
            "login": payload["login"],
            "password": payload["password"]
        }).json()["id"]

        # проверяем, что курьер создался
        assert payload is not None

        # удаляем курьера
        delete_courier(courier_id)

    @allure.title("Создание курьера с уже существующим логином")
    def test_create_courier_with_existing_login(self):
        # создаём курьера
        payload = register_new_courier()
        courier_id = requests.post(BASE_URL + "/api/v1/courier/login", data={
            "login": payload["login"],
            "password": payload["password"]
        }).json()["id"]

        # повторная попытка создать с тем же логином
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]

        # удаляем курьера
        delete_courier(courier_id)

    @allure.title("Создание курьера без обязательного поля 'password'")
    def test_create_courier_without_password(self):
        payload = {
            "login": "testLogin",
            "firstName": "TestCourier"
        }
        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 400

    @allure.title("Создание курьера без обязательного поля 'login'")
    def test_create_courier_without_login(self):
        payload = {
            "password": "12345",
            "firstName": "TestName"
        }

        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 400