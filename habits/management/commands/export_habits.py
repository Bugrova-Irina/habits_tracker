from email.policy import default

from django.core import serializers
from django.core.management import BaseCommand

from habits.models import Habit


class Command(BaseCommand):
    help = "Export habits to JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--output", type=str, default="habits_export.json", help="Output file name"
        )

    def handle(self, *args, **options):
        output_file = options["output"]
        habits = Habit.objects.all()

        with open(output_file, "w", encoding="utf-8") as f:
            serializers.serialize("json", habits, stream=f)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully exported {len(habits)} habits to {output_file}"
            )
        )
