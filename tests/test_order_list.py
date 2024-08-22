from api.api_orders import OrdersApi
from api.api_users import UsersApi
from tests.data import AUTH_ERROR_TEXT
import allure


class TestOrdersList:

    @allure.title('Получение списка заказов неавторизованным пользователем')
    @allure.description('Проверяем, что запрос без авторизации вернет код 401 и нужное сообщение в теле ответа ')
    def test_get_orders_list_by_non_auth_user(self):
        response = OrdersApi.get_orders_list()
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == AUTH_ERROR_TEXT

    @allure.title('Получение заказов авторизованного пользователя')
    @allure.description('Проверяем, что запрос c авторизацией вернет код 200 и нужными данными в теле ответа')
    def test_get_orders_list_by_auth_user(self, user):
        UsersApi.create_user(user)
        response = UsersApi.login_user(user)
        assert response.status_code == 200
        token = response.json()['accessToken']
        response = OrdersApi.get_orders_list(token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["orders"] == []
        assert response.json()["total"] > 0
        UsersApi.delete_user(token)
