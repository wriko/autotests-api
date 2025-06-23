from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()  # Получаем экземпляр PublicUsersClient с уже настроенным HTTP-клиентом

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email = get_random_email(),
    password = "string",
    last_name = "string",
    first_name = "string",
    middle_name ="string"
)

# Отправляем POST запрос на создание пользователя (метод create_user)
create_user_response = public_users_client.create_user(create_user_request)  # Создаем пользователя с помощью метода create_user и сохраняем ответ в переменную create_user_response
print(f"Создан пользователь: {create_user_response}")

# Инициализируем клиенты
autentication_user = AuthenticationUserSchema(
    email = create_user_request.email,
    password = create_user_request.password
)
files_client = get_files_client(autentication_user) # Получаем экземпляр FilesClient с уже настроенным HTTP-клиентом и передаем в него данные для аутентификации
courses_client = get_courses_client(autentication_user) # Получаем экземпляр CoursesClient с уже настроенным HTTP-клиентом и передаем в него данные для аутентификации

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    filename = "image.png",
    directory = "courses",
    upload_file = "./testdata/files/image.png"  # Путь к файлу, который нужно загрузить
)

create_file_response = files_client.create_file(create_file_request) # Создаем файл с помощью метода create_file и сохраняем ответ в переменную create_file_response
print(f"Cоздан файл: {create_file_response}")

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title = "Python",
    maxScore = 100,
    minScore = 10,
    description = "Python API Course",
    estimatedTime = "2 weeks",
    previewFileId = create_file_response.file.id,
    createdByUserId = create_user_response.users.id
)

create_course_response = courses_client.create_course(create_course_request) # Создаем курс с помощью метода create_course и сохраняем ответ в переменную create_course_response
print(f"Cоздан курс: {create_course_response}")
