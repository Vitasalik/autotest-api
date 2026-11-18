from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    public_user_client = get_public_users_client()

    request_user = CreateUserRequestSchema()

    public_user_client.create_user(request_user)

    authentication_client = get_authentication_client()

    request_login = LoginRequestSchema(
        email=request_user.email,
        password=request_user.password,
    )

    login_response = authentication_client.login_api(request=request_login)
    login_responser_data = LoginResponseSchema.model_validate_json(login_response.text)


    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_responser_data)
    validate_json_schema(login_response.json(), login_responser_data.model_json_schema())