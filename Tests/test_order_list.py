import requests
import allure
from data import BASE_URL, ORDER_LIST_PATH

@allure.feature("Список заказов")
class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        with allure.step("Запрос списка заказов"):
            response = requests.get(BASE_URL + ORDER_LIST_PATH)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)