import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
from decimal import Decimal


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            temp_date = datetime.strptime(phone['release_date'], "%Y-%m-%d").date()
            save_str = Phone(
                id=int(phone['id']),
                name=phone['name'],
                price=Decimal(phone['price'].replace(',', '.')),
                image=phone['image'],
                release_date=temp_date,
                lte_exists=bool(phone['lte_exists'])
            )
            save_str.save()
