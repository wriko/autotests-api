# теперь мы можем переписать то, что было написано в httpx_get_user.py, используя созданные клиенты PublicUsersClient и PrivateUsersClient.

from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from clients.private_http_builder import AuthenticationUserDict
from tools.fakers import get_random_email


# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()  # Получаем экземпляр PublicUsersClient с уже настроенным HTTP-клиентом

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
    email = get_random_email(),
    password = "string",
    lastName = "string",
    firstName = "string",
    middleName ="string"
)
# Отправляем POST запрос на создание пользователя (метод create_user)
create_user_response = public_users_client.create_user(create_user_request)  # Создаем пользователя с помощью метода create_user и сохраняем ответ в переменную create_user_response
print(f"Создан пользователь: {create_user_response}")

# Инициализируем пользовательские данные для аутентификации
autentication_user = AuthenticationUserDict( # Создаем объект аутентификации пользователя в формате AuthenticationUserDict для удобства чтения и проверки его содержимого
    email = create_user_request['email'],
    password = create_user_request['password']
)

# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(autentication_user)

# Отправляем GET запрос на получение данных пользователя (метод get_user)
get_user_response = private_users_client.get_user(create_user_response['user']['id'])  # Получаем пользователя по ID с помощью метода get_user_api из private_users_client
print(f"Получен пользователь: {get_user_response}")