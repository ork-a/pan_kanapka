from django.core.management.base import BaseCommand
from sandwiches.models import Sandwich


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, **options):
        sample_data = (
            ('z tunczykiem', 12),
            ('z awokado', 7),
            ('z pietruszka', 5),
        )

        sandwich = Sandwich()
        for name, price in sample_data:
            sandwich.name = name
            sandwich.price = price
            sandwich.save()
