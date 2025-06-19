from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict
from typing import TypedDict


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    autentication_client = get_authentication_client()

    login_request = LoginRequestDict(email=user["email"], password=user["password"])
    login_response = autentication_client.login(login_request)

    return Client(base_url='http://localhost:8000/',
                  timeout=100,
                  headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
                  )