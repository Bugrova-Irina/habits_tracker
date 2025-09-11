from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    """Создание привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # Назначение пользователя владельцем привычки
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    """Вывод списка привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Вывод страницы привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitUpdateAPIView(UpdateAPIView):
    """Обновление привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyAPIView(DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
