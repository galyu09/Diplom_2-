from api.api_users import UsersApi
from tests import data
from tests.data import *
import pytest
import allure


class TestUserCreate:
    @allure.title('Успешное создание юзера')
    @allure.description('Проверяем, что запрос возвращает валидный код ответа 200 и ожидаемое тело ответа')
    def test_create_user_unique(self, user):
        response_create_user = UsersApi.create_user(user)
        response = response_create_user.json()
        assert user['name'] == response['user']['name']
        assert user['email'] == response['user']['email']
        assert response['success'] is True
        UsersApi.delete_user(response['accessToken'])

    @allure.title('Создание дублирующего юзера')
    @allure.description('Проверяем, что запрос вернет код 403 и ожидаемое тело ответа')
    def test_create_double_user(self, user):
        response_create_user = UsersApi.create_user(user)
        response_create_double_user_error = UsersApi.create_user(user)
        assert response_create_double_user_error.status_code == 403
        assert response_create_double_user_error.json()['message'] == DOUBLE_USER_ERROR
        UsersApi.delete_user(response_create_user.json()['accessToken'])

    @allure.title('Ошибка запроса на создание юзера без одного из параметра')
    @allure.description('Проверяем, что запрос без обязательного параметра вернут код 403 и ожидаемое тело ответа')
    @pytest.mark.parametrize(
        'payload',
        (
            pytest.param(data.USER_EMPTY_EMAIL, id='empty_email'),
            pytest.param(data.USER_EMPTY_PASSWORD, id='empty_password'),
            pytest.param(data.USER_EMPTY_NAME, id='empty_name')
        )
    )
    def test_create_user_without_required_field(self, payload):
        response = UsersApi.create_user(payload)
        assert response.status_code == 403
        assert response.json()['message'] == AUTH_REQUIRED_ERROR

