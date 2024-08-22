import requests
import allure
from tests.urls import Urls


class OrdersApi:

    @staticmethod
    @allure.step('Отправка запроса на создание заказ')
    def create_order(body, token=None):
        headers = {'Authorization': token} if token else None
        response = requests.post(Urls.ORDER_CREATE, json=body, headers=headers)
        return response

    @staticmethod
    @allure.step('Отправка запроса на получение списка заказов')
    def get_orders_list(token=None):
        headers = {'Authorization': token} if token else None
        response = requests.get(Urls.ORDERS_LIST, headers=headers)
        return response




