from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_telegram_message_about_habit():
    """Отправка напоминаний в телеграмм"""
    today = timezone.now().date()
    habits = Habit.objects.filter(owner__isnull=False, habit_time=today)

    for habit in habits:
        message = (
            f"Напоминание о привычке {habit.to_do}. "
            f"Время выполнения: {habit.execution_time} секунд. "
            f"Место: {habit.place}."
        )

        if habit.owner.tg_chat_id:
            send_telegram_message(habit.owner.tg_chat_id, message)
