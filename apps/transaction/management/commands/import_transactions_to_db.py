from django.core.management import BaseCommand
from django.conf import settings

from db.database import Database


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(getattr(settings, "BASE_DIR") / 'transaction.agz', 'rb') as f:
            database = Database().get_db()
            database["transaction"].insert_many((f.read()))
