import grpc  # импортирует модуль `grpc`, который используется для работы с gRPC
from concurrent import futures  # импортирует `futures` для создания пула потоков
import course_service_pb2  # импортирует модуль `course_service_pb2`, который содержит определения сообщений и сервисов, сгенерированные из файла course_service.proto
import course_service_pb2_grpc  # импортирует модуль `course_service_pb2_grpc`, который содержит определения сервисов, сгенерированные из файла course_service.proto


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer): # определяет класс `CourseServiceServicer`, который наследуется от `course_service_pb2_grpc.CourseServiceServicer`.
    def GetCourse(self, request, context): # определяет метод `GetCourse`, который принимает запрос `request` и контекст `context`.
        return course_service_pb2.GetCourseResponse( # возвращает сообщение `GetCourseResponse` с информацией о курсе.
            course_id=request.course_id, # идентификатор курса, полученный из запроса
            title="Автотесты API", # заголовок курса
            description="Будем изучать написание API автотестов" # описание курса
        )


def serve(): # определяет функцию `serve`, которая запускает gRPC сервер.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # создает экземпляр сервера gRPC с использованием пула потоков с максимальным количеством 10 потоков.
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server) # регистрирует `CourseServiceServicer` на сервере, чтобы он мог обрабатывать запросы к сервису `CourseService`.
    server.add_insecure_port('[::]:50051') # добавляет небезопасный порт для сервера, чтобы он слушал на всех интерфейсах по порту 50051.
    server.start() # запускает сервер, чтобы он начал принимать входящие запросы.
    print("gRPC сервер запущен на порту 50051...")
    server.wait_for_termination() # ожидает завершения работы сервера, чтобы он продолжал работать до тех пор, пока не будет остановлен вручную.


if __name__ == "__main__": # проверяет, является ли этот файл основным модулем, и если да, то запускает функцию serve.
    serve() # проверяет, является ли этот файл основным модулем, и если да, то запускает функцию serve.
