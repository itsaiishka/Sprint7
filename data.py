BASE_URL = "https://qa-scooter.praktikum-services.ru"

CREATE_COURIER_PATH = "/api/v1/courier"
LOGIN_COURIER_PATH = "/api/v1/courier/login"
CREATE_ORDER_PATH = "/api/v1/orders"
ORDER_LIST_PATH = "/api/v1/orders"

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