import allure
from api.api_users import UsersApi
from tests.data import USER_LOGIN_ERROR


class TestUserLogin:
    @allure.title('Логин существующим юзером')
    @allure.description(
        'Проверяем, что валидный запрос на логин существующим юзером возвращает код 200 и нужными данными в теле ответа')
    def test_user_login_sucsess(self, user):
        UsersApi.create_user(user)
        response = UsersApi.login_user(user)
        response = response.json()
        access_token = response['accessToken']
        assert user['name'] == response['user']['name']
        assert user['email'] == response['user']['email']
        assert response['success'] is True
        UsersApi.delete_user(access_token)


    @allure.title('Логин c некорректными данными')
    @allure.description('Проверяем, что запрос на логин с некорректными данными вернет код 403 и ошибкой в теле ответа')
    def test_user_login_wrong_data(self, user):
        response = UsersApi.login_user(user)
        assert response.status_code == 401
        assert response.json()['message'] == USER_LOGIN_ERROR






