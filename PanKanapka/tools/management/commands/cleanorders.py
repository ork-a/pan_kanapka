from django.core.management.base import BaseCommand
from tools.csv2db import DbManager

class Command(BaseCommand):
    help = 'Clean orders databases'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, **options):
        db_manager = DbManager()
        db_manager.delete_orders()
        self.stdout.write(self.style.SUCCESS('Orders deleted'))