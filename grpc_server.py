import grpc  # импортирует модуль `grpc`, который используется для работы с gRP
from concurrent import futures  # импортирует `futures` для создания пула потоков
import user_service_pb2 #  импортирует модуль `user_service_pb2`, который содержит определения сообщений и сервисов, сгенерированные из файла `user_service.proto
import user_service_pb2_grpc # импортирует модуль `user_service_pb2_grpc`, который содержит определения сервисов, сгенерированные из файла `user_service.proto`.

class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer): # определяет класс `UserServiceServicer`, который наследуется от `user_service_pb2_grpc.UserServiceServicer`.
    def GetUser(self, request, context): # определяет метод `GetUser`, который принимает запрос `request` и контекст `context`.
        print(f"Получен запрос к методу GetUser от пользователя: {request.username}")
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!") # возвращает сообщение `GetUserResponse` с приветствием для пользователя.


def Serve(): # определяет функцию `Serve`, которая запускает gRPC сервер.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # создает gRPC сервер с пулом потоков, который может обрабатывать до 10 одновременных запросов.
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server) # регистрирует `UserServiceServicer` на сервере.
    server.add_insecure_port('[::]:50051') # добавляет небезопасный порт для сервера, чтобы он слушал на всех интерфейсах по порту 50051.
    server.start() # запускает сервер.
    print("gRPC сервер запущен на порту 50051...") # выводит сообщение о запуске сервера.
    server.wait_for_termination() # ожидает завершения работы сервера, чтобы он продолжал работать до тех пор, пока не будет остановлен вручную.


if __name__ == "__main__": # проверяет, является ли этот файл основным модулем, и если да, то запускает функцию Serve.
    Serve() # запускает gRPC сервер, который будет слушать на порту 50051 и обрабатывать запросы к сервису UserService.