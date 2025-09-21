from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    is_nice_habit = serializers.BooleanField(
        required=False,
        allow_null=True,
    )
    reward = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    related_habit = serializers.PrimaryKeyRelatedField(
        required=False, allow_null=True, queryset=Habit.objects.all()
    )
    execution_time = serializers.IntegerField(
        required=False, allow_null=True, min_value=1, max_value=120
    )

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        # Получаем текущие значения из instance, если он существует
        instance = getattr(self, "instance", None)

        # Для частичных обновлений используем текущие значения полей, если они не переданы
        is_nice_habit = attrs.get("is_nice_habit")
        if is_nice_habit is None and instance:
            is_nice_habit = instance.is_nice_habit

        reward = attrs.get("reward")
        if reward is None and instance:
            reward = instance.reward

        related_habit = attrs.get("related_habit")
        if related_habit is None and instance:
            related_habit = instance.related_habit

        execution_time = attrs.get("execution_time")
        if execution_time is None and instance:
            execution_time = instance.execution_time

        # Проверка 1: нельзя одновременно указывать вознаграждение и связанную привычку
        if reward and related_habit:
            raise serializers.ValidationError(
                "Нельзя одновременно указывать вознаграждение и связанную привычку"
            )
        # Проверка 2: если привычка приятная, у нее не может быть вознаграждения или связанной привычки
        if is_nice_habit:
            if reward:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть вознаграждения"
                )
            if related_habit:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть связанной привычки"
                )
            # Для приятных привычек время выполнения должно быть null
            if execution_time is not None:
                raise serializers.ValidationError(
                    "У приятной привычки не должно быть времени выполнения"
                )
        else:
            # Для полезных привычек время выполнения обязательно и не более 120 секунд
            if execution_time is None:
                raise serializers.ValidationError(
                    "Для полезной привычки необходимо указать время выполнения"
                )
            if execution_time > 120:
                raise serializers.ValidationError(
                    "Время выполнения полезной привычки должно быть не более 120 секунд"
                )

        # Проверка 3: связанная привычка должна быть приятной
        if related_habit and not related_habit.is_nice_habit:
            raise serializers.ValidationError(
                "Связанной привычкой может быть только приятная привычка"
            )

        return attrs
