import pytest
import allure
from api.api_users import UsersApi
from tests.data import AUTH_ERROR_TEXT


class TestUserChange:
    @allure.title('Изменение данных пользователя с авторизацией')
    @allure.description('Проверяем успешное изменение параметров пользователя: возвращается код ответа 200 и нужное тело ответа')
    @pytest.mark.parametrize(
        'case',
        (
                pytest.param('password', id='new_password'),
                pytest.param('name', id='new_name')
        )
    )
    def test_user_change_with_auth(self, user, case):
        UsersApi.create_user(user)
        response = UsersApi.login_user(user)
        token = response.json()['accessToken']
        user[case] = 'new_' + user[case]
        response = UsersApi.change_user_data(user, token)
        assert response.status_code == 200
        response = response.json()
        assert user['name'] == response['user']['name']
        assert user['email'] == response['user']['email']
        assert response['success'] is True
        UsersApi.delete_user(token)


    @allure.title('Изменение данных пользователя без авторизацией')
    @allure.description('Проверяем, что при отправке запроса без авторизации возвращается код ответа 200 и нужное тело ответа')
    @pytest.mark.parametrize(
        'case',
        (
                pytest.param('password', id='new_password'),
                pytest.param('name', id='new_name')
        )
    )
    def test_user_change_without_auth(self, user, case):
        UsersApi.create_user(user)
        user[case] = 'new_' + user[case]
        response = UsersApi.change_user_data(user)
        assert response.status_code == 401
        assert response.json()['message'] == AUTH_ERROR_TEXT