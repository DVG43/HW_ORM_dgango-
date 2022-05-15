import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            any_phone = Phone.obgects.update_or_create(
            name=phone['name'],
            image=phone['image'],
            prise=phone['price'],
            relaese_data=phone['release_date'],
            lte_exist=phone['lte_exists']
            )

        pass
