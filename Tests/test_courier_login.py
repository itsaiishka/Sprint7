import requests
from data import BASE_URL, LOGIN_COURIER_PATH
import allure

@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.title("Успешный вход курьера с валидными данными")
    def test_courier_login_success(self, courier):
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={
            "login": courier["login"],
            "password": courier["password"]
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Вход курьера с несуществующим логином")
    def test_courier_login_with_nonexistent_login(self):
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={
            "login": "nonexistentuser",
            "password": "1234"
        })
        assert response.status_code == 404

    @allure.title("Вход курьера с неверным паролем")
    def test_courier_login_with_wrong_password(self, courier):
        response = requests.post(BASE_URL + LOGIN_COURIER_PATH, data={
            "login": courier["login"],
            "password": "wrongPassword"
        })
        assert response.status_code == 404