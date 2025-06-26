from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema


# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()  # Получаем экземпляр PublicUsersClient с уже настроенным HTTP-клиентом

# Создаем пользователя
create_user_request = CreateUserRequestSchema() # Создаем объект запроса на создание пользователя. Сами поля будут заполнены случайными данными с помощью фабрик, определенных в классе CreateUserRequestSchema

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
exercises_client = get_exercises_client(autentication_user) # Получаем экземпляр ExercisesClient с уже настроенным HTTP-клиентом и передаем в него данные для аутентификации

# Загружаем файл
create_file_request = CreateFileRequestSchema(upload_file = "./testdata/files/image.png") # Создаем объект запроса на создание файла. Сами поля будут заполнены случайными данными с помощью фабрик, определенных в классе CreateFileRequestSchema # Путь к файлу, который нужно загрузить)
create_file_response = files_client.create_file(create_file_request) # Создаем файл с помощью метода create_file и сохраняем ответ в переменную create_file_response
print(f"Create file data: {create_file_response}")

# Создаем курс
create_course_request = CreateCourseRequestSchema( # Создаем объект запроса на создание курса. Сами поля будут заполнены случайными данными с помощью фабрик, определенных в классе CreateCourseRequestSchema, кроме полей, которые мы передаем явно
    preview_file_id = create_file_response.file.id,
    created_by_user_id = create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request) # Создаем курс с помощью метода create_course и сохраняем ответ в переменную create_course_response
print(f"Create course data: {create_course_response}")

# Создаем задание
create_exercise_request = CreateExerciseRequestSchema(course_id = create_course_response.course.id) # Создаем объект запроса на создание задания. Сами поля будут заполнены случайными данными с помощью фабрик, определенных в классе CreateExerciseRequestSchema, кроме поля course_id, которое мы передаем явно

create_exercise_response = exercises_client.create_exercise(create_exercise_request) # Создаем задание с помощью метода create_exercise и сохраняем ответ в переменную create_exercise_response
print(f"Create exercise data: {create_exercise_response}") # Выводим данные о созданном задании