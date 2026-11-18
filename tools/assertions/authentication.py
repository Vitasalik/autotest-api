from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_equal(response.token.token_type, 'bearer', 'Token type')
    assert_is_true(response.token.access_token, 'Access token')
    assert_is_true(response.token.refresh_token, 'Refresh token')