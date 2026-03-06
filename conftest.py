import pytest
import requests
from helpers import register_new_courier, delete_courier
from data import BASE_URL, LOGIN_COURIER_PATH

@pytest.fixture
def courier():
    
    courier_data = register_new_courier()

    response = requests.post(
        BASE_URL + LOGIN_COURIER_PATH,
        data={
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
    )

    courier_id = response.json()["id"]

    yield courier_data

    delete_courier(courier_id)