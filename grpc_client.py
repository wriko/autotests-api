import grpc # импортирует модуль `grpc`, который используется для работы с gRPC

import user_service_pb2 # импортирует модуль `user_service_pb2`, который содержит определения сообщений и сервисов, сгенерированные из файла `user_service.proto`.
import user_service_pb2_grpc # импортирует модуль `user_service_pb2_grpc`, который содержит определения сервисов, сгенерированные из файла `user_service.proto`.


channel = grpc.insecure_channel('localhost:50051')  # создает небезопасный канал связи с сервером gRPC, который работает на локальном хосте и порту 50051.
stub = user_service_pb2_grpc.UserServiceStub(channel)  # создает объект `stub`, который позволяет вызывать методы сервиса `UserService` на сервере gRPC через созданный канал.


response = stub.GetUser(user_service_pb2.GetUserRequest(username='Alice')) # вызывает удаленную процедуру `GetUser` на сервере gRPC, передавая сообщение `GetUserRequest` с именем пользователя 'Alice'. Результат вызова сохраняется в переменной `response`.
print(response)