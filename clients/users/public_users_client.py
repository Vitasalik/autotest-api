from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    last_name: str
    first_name: str
    middle_name: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с email, password, last_name, first_name, middle_name.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url='/api/v1/users', json=request)
