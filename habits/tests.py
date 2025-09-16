from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование CRUD привычек"""

    def setUp(self):
        # Экземпляр пользователя
        self.user = User.objects.create(email="admin@example.com")
        # Экземпляр привычки
        self.habit = Habit.objects.create(
            is_nice_habit=False,
            reward=None,
            related_habit=None,
            execution_time=120,
            to_do="do exercises",
            place="at home",
            habit_time="2025-09-16",
            periodicity="every_day",
            general_access=True,
            owner=self.user,
        )
        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        # Проверяем вывод информации о привычке
        url = reverse("habits:habit-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("to_do"), self.habit.to_do)

    def test_habit_create(self):
        # Проверяем создание привычки
        url = reverse("habits:habit-create")
        data = {
            "to_do": "sleep at 21:00",
            "is_nice_habit": False,
            "execution_time": 120,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        # Проверяем обновление информации о привычке
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {"to_do": "sleep at 21:01"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("to_do"), "sleep at 21:01")

    def test_habit_delete(self):
        # Проверяем удаление привычки
        url = reverse("habits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habits_list(self):
        # Проверяем вывод списка привычек
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "execution_time": 120,
                    "general_access": True,
                    "habit_time": "2025-09-16",
                    "id": 6,
                    "is_nice_habit": False,
                    "owner": 5,
                    "periodicity": "every_day",
                    "place": "at home",
                    "related_habit": None,
                    "reward": None,
                    "to_do": "do exercises",
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
