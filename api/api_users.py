import requests
import allure
from tests.urls import Urls


class UsersApi:
    @staticmethod
    @allure.step('Создаем пользователя')
    def create_user(payload):
        response = requests.post(Urls.USER_CREATE, json=payload)
        return response

    @staticmethod
    @allure.step('Логинимся юзером')
    def login_user(payload):
        response = requests.post(Urls.USER_LOGIN, json=payload)
        return response

    @staticmethod
    @allure.step('Удаляем юзера')
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(Urls.USER_CHANGE, headers=headers)

    @staticmethod
    @allure.step('Изменяем данные юзера')
    def change_user_data(payload, token=None):
        headers = {'Authorization': token} if token else None
        return requests.patch(Urls.USER_CHANGE, json=payload, headers=headers)

