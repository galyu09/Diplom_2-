import pytest

from tests.utils import generate_random_string


@pytest.fixture
def user():
    return {
        'email': generate_random_string(10)+'@mail.ru',
        'password': generate_random_string(10),
        'name': generate_random_string(10)
    }

