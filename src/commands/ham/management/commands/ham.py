from django.core.management.base import BaseCommand
from libs.random.random import Random

class Command(BaseCommand):
    help = "hamコマンド"

    def handle(self, *args, **options):
        print(f'Hello ham! {Random.get_random_int()}')
