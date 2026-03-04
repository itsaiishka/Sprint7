import requests
import pytest
import allure
import copy
from data import BASE_URL, CREATE_ORDER_PATH

order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha",
    "metroStation": 4,
    "phone": "+79999999999",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Test order"
}
    
@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с валидными данными")
    def test_create_order_with_different_colors(self, color):
        body = copy.deepcopy(order_body)
        body["color"] = color

        with allure.step(f"Создаём заказ с цветами: {color}"):
            response = requests.post(BASE_URL + CREATE_ORDER_PATH, json=body)

        assert response.status_code == 201
        assert "track" in response.json()