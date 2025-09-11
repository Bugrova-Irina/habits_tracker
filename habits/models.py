from django.db import models


class Habit(models.Model):
    """Модель полезной привычки"""

    # Периодичность
    EVERY_DAY = "every_day"
    ONCE_EVERY_2_DAYS = "once_every_2_days"
    ONCE_EVERY_3_DAYS = "once_every_3_days"
    ONCE_EVERY_4_DAYS = "once_every_4_days"
    ONCE_EVERY_5_DAYS = "once_every_5_days"
    ONCE_EVERY_6_DAYS = "once_every_6_days"
    ONCE_EVERY_7_DAYS = "once_every_7_days"
    PERIODICITY_CHOICES = [
        (EVERY_DAY, "Каждый день"),
        (ONCE_EVERY_2_DAYS, "Раз в 2 дня"),
        (ONCE_EVERY_3_DAYS, "Раз в 3 дня"),
        (ONCE_EVERY_4_DAYS, "Раз в 4 дня"),
        (ONCE_EVERY_5_DAYS, "Раз в 5 дней"),
        (ONCE_EVERY_6_DAYS, "Раз в 6 дней"),
        (ONCE_EVERY_7_DAYS, "Раз в 7 дней"),
    ]

    to_do = models.CharField(
        max_length=250,
        verbose_name="Что нужно сделать",
        help_text="Укажите, что нужно сделать",
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Владелец привычки",
        help_text="Укажите владельца привычки",
    )
    place = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Место, где нужно сделать",
        help_text="Укажите место, где нужно сделать",
    )
    habit_time = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Время, когда нужно сделать",
        help_text="Укажите время, когда нужно сделать",
    )
    periodicity = models.CharField(
        max_length=17,
        choices=PERIODICITY_CHOICES,
        default=EVERY_DAY,
        verbose_name="Как часто нужно делать",
        help_text="Укажите, как часто нужно делать",
    )
    is_nice_habit = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="Признак приятной привычки",
        help_text="Укажите признак привычки",
    )
    reward = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
    )
    execution_time = models.PositiveIntegerField(
        default=120,
        blank=True,
        null=True,
        verbose_name="Время выполнения полезной привычки",
        help_text="Укажите время выполнения привычки (не более 120 секунд)",
    )
    general_access = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="Доступна всем",
        help_text="Укажите доступность привычки",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.to_do
