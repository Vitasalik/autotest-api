from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнения.
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка упражнений.
    """
    exercises: list[Exercise]


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления упражнения.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения курса.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url='/api/v1/exercises', params=query)

    def create_exersice_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, description, estimatedTime, orderIndex
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url='/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesRequestDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exersice_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(users: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(users))
