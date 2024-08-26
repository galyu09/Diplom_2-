import allure

from api.api_orders import OrdersApi
from api.api_users import UsersApi
from tests import data
from tests.data import ORDER_ERROR_TEXT


class TestOrderCreate:
    @allure.title('Отправка заказа')
    @allure.description('Проверяем, что при валидном запросе авторизованным пользователем возвращается код ответа 200 и нужное тело')
    def test_order_create_by_auth_user(self, user):
        UsersApi.create_user(user)
        response = UsersApi.login_user(user)
        token = response.json()['accessToken']
        response = OrdersApi.create_order(data.ORDER_DATA_VALID, token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()['order']['number'] is not None
        assert response.json()['order']['number'] > 0
        UsersApi.delete_user(token)

    @allure.title('Отправка заказа неавторизованным юзером')
    @allure.description(
        'ОР: запрос НЕавторизованным пользователем возвращает код 401 и нужное тело ответа'
        'ФР: дает отправить заказ неавторизованному пользователю - известный баг')
    def test_order_create_by_user_unauth(self):
        response = OrdersApi.create_order(data.ORDER_DATA_VALID)
        assert response.status_code == 401
        assert response.json()["success"] is False

    @allure.title('Запрос на отправку пустого заказа без ингридиентов')
    @allure.description('Проверяем, что при отправке пустого заказа вернется код 400 и нужный текст ошибки в теле')
    def test_create_empty_orders(self):
        response = OrdersApi.create_order(data.ORDER_EMPTY)
        assert response.status_code == 400
        assert response.json()["message"] == ORDER_ERROR_TEXT

    @allure.title('Запрос на отправку заказа с неверным хэшем ингридиентов')
    @allure.description('Проверяем, что при отправке заказа c неверным хешем вернется код 500 и нужный текст ошибки в теле')
    def test_order_create_invalid_ingridients(self, user):
        UsersApi.create_user(user)
        response = UsersApi.login_user(user)
        token = response.json()['accessToken']
        response = OrdersApi.create_order(data.ORDER_DATA_INVALID, token)
        assert response.status_code == 500
        UsersApi.delete_user(token)




