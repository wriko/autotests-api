import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import function_user, UserFixture



class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: ExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
    exercises_client: ExercisesClient, function_user: UserFixture, function_course: CourseFixture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)