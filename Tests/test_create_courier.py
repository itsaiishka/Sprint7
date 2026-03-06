import requests
from data import BASE_URL, CREATE_COURIER_PATH, LOGIN_COURIER_PATH
import allure
from helpers import delete_courier

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Создание курьера с валидными данными")
    def test_create_courier_success(self, courier):

        response = requests.post(
            BASE_URL + LOGIN_COURIER_PATH,
            data={
                "login": courier["login"],
                "password": courier["password"]
            }
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Создание курьера с уже существующим логином")
    def test_create_courier_with_existing_login(self, courier):

        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": "TestCourier"
        }

        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]

    @allure.title("Создание курьера без обязательного поля 'password'")
    def test_create_courier_without_password(self):
        payload = {
            "login": "testLoginNoPass",
            "firstName": "TestCourier"
        }

        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)
    
        #Постусловие: удалить курьера, если он вдруг создался
        try:
            response_login = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={
                "login": payload["login"],
                "password": "12345"
            })
            if response_login.status_code == 200:
                courier_id = response_login.json()["id"]
                delete_courier(courier_id)
        except Exception:
            pass
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Создание курьера без обязательного поля 'login'")    
    def test_create_courier_without_login(self):
        payload = {
            "password": "12345",
            "firstName": "TestCourier"
        }

        response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

        assert response.status_code == 400
        assert "message" in response.json()