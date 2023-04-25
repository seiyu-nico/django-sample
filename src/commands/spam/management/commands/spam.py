from django.core.management.base import BaseCommand
from libs.random.random import Random

class Command(BaseCommand):
    help = "spamコマンド"

    def handle(self, *args, **options):
        print(f'Hello spam! {Random.get_random_int()}')
