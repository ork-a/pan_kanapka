from django.core.management.base import BaseCommand
from tools.csv2db import DbManager

class Command(BaseCommand):
    help = 'Fills database with sample data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, **options):
        db_manager = DbManager()
        db_manager.delete_all()
        self.stdout.write(self.style.SUCCESS('Databases cleaned'))
        db_manager.import_allergens()
        self.stdout.write(self.style.SUCCESS('Allergens populated'))
        db_manager.import_ingredient_groups()
        self.stdout.write(self.style.SUCCESS('Ingredient groups populated'))
        db_manager.import_ingredients()
        self.stdout.write(self.style.SUCCESS('Ingredients populated'))
        db_manager.import_sandwiches()
        self.stdout.write(self.style.SUCCESS('Sandwiches populated'))
        db_manager.import_companies()
        self.stdout.write(self.style.SUCCESS('Companies populated'))
        db_manager.import_clients()
        self.stdout.write(self.style.SUCCESS('Clients populated, admin user: admin@kanapka.com, password: admin'))
        db_manager.create_statuses()
        self.stdout.write(self.style.SUCCESS('Order statuses populated'))