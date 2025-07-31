import grpc  # импортирует модуль `grpc`, который используется для работы с gRPC

import course_service_pb2  # импортирует модуль `course_service_pb2`, который содержит определения сообщений и сервисов, сгенерированные из файла course_service.proto
import course_service_pb2_grpc  # импортирует модуль `course_service_pb2_grpc`, который содержит определения сервисов, сгенерированные из файла course_service.proto

channel = grpc.insecure_channel('localhost:50051')  # создает небезопасный канал связи с сервером gRPC, который работает на локальном хосте и порту 50051.
stub = course_service_pb2_grpc.CourseServiceStub(channel)  # создает объект `stub`, который позволяет вызывать методы сервиса `UserService` на сервере gRPC через созданный канал.



response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course")) # вызывает удаленную процедуру `GetCourse` на сервере gRPC, передавая сообщение `GetCourseRequest` с идентификатором курса 'api-course'. Результат вызова сохраняется в переменной `response`.
print(response)
