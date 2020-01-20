from django.core.management.base import BaseCommand
from students.models import Group


class Command(BaseCommand):
    help = 'Generate 10 random groups'

    def handle(self, *args, **options):

        for _ in range(10):
            Group.generate_group()
