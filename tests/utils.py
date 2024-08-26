import random
import allure
import string

from api.api_orders import OrdersApi


@allure.step('генерируем тестовые данные для залогина')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

