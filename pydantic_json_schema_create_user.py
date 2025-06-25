from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake



# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()  # Получаем экземпляр PublicUsersClient с уже настроенным HTTP-клиентом

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email = fake.email(),
    password = "string",
    last_name = "string", # Передаем аргументы в формате snake_case вместо camelCase
    first_name = "string", # Передаем аргументы в формате snake_case вместо camelCase
    middle_name = "string" # Передаем аргументы в формате snake_case вместо camelCase
)


# Генерация JSON схемы для создания пользователя
create_user_response = public_users_client.create_user_api(create_user_request)

# Получаем JSON схему из модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

# Проверяем, что JSON ответ от API соответствует ожидаемой JSON схеме
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)