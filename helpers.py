import requests
import random
import string
from data import BASE_URL, CREATE_COURIER_PATH

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier():
    login = generate_random_string()
    password = generate_random_string()
    first_name = "TestCourier"

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(BASE_URL + CREATE_COURIER_PATH, data=payload)

    if response.status_code == 201:
        return payload  
    else:
        raise Exception(f"Failed to create courier: {response.status_code} - {response.text}")

def delete_courier(courier_id):
    response = requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")
    if response.status_code != 200:
        print(f"Warning: failed to delete courier {courier_id}")