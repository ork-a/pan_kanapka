from django.core.management.base import BaseCommand
from tools.csv2db import DbManager

class Command(BaseCommand):
    help = 'Wipes databases'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, **options):
        db_manager = DbManager()
        db_manager.delete_clients()
        self.stdout.write(self.style.SUCCESS('Clients deleted, except admin@kanapka.com'))
        db_manager.delete_companies()
        self.stdout.write(self.style.SUCCESS('Companies deleted'))
        db_manager.delete_allergens()
        self.stdout.write(self.style.SUCCESS('Allergens deleted'))
        db_manager.delete_ingredients()
        self.stdout.write(self.style.SUCCESS('Ingredients deleted'))
        db_manager.delete_ingredient_groups()
        self.stdout.write(self.style.SUCCESS('Ingredient groups deleted'))
        db_manager.delete_sandwiches()
        self.stdout.write(self.style.SUCCESS('Sandwiches deleted'))
