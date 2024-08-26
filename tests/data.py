from typing import Dict

USER_EMPTY_EMAIL = {'email': '', 'password': 'password', 'name': 'Galina_qa_diplom2'}
USER_EMPTY_PASSWORD = {'email': 'Galina_qa_diplom2@yandex.ru', 'password': '', 'name': 'Galina_qa_diplom2'}
USER_EMPTY_NAME = {'email': 'Galina_qa_diplom2@yandex.ru', 'password': 'password', 'name': ''}

USER_WRONG_EMAIL = {
    'email': 'Galina_WRONG@yandex.ru',
    'password': 'password',
    'name': 'Galina_qa_diplom2'
}
USER_WRONG_PASSWORD = {
    'email': 'Galina_qa_diplom2@yandex.ru',
    'password': 'WRONG',
    'name': 'Galina_qa_diplom2'
}

USER_DATA_VALID = {
    'email': 'Galina_qa_diplom2@yandex.ru',
    'password': 'password',
    'name': 'Galina_qa_diplom2'
}

# Набор тестовых данных для заказа
ORDER_DATA_VALID = {
    "ingredients": [
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa70",
        "61c0c5a71d1f82001bdaaa73"
    ]
}
ORDER_EMPTY = {
    "ingredients": []
}

ORDER_DATA_INVALID = {
    "ingredients": ["i'm bun", "i'm meat", "i'm sauce"]
}

DOUBLE_USER_ERROR = 'User already exists'
AUTH_REQUIRED_ERROR = 'Email, password and name are required fields'
USER_LOGIN_ERROR = 'email or password are incorrect'
ORDER_ERROR_TEXT = 'Ingredient ids must be provided'
AUTH_ERROR_TEXT = 'You should be authorised'

