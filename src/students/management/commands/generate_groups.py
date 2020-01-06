from django.core.management.base import BaseCommand, CommandError
from students.models import Group

class Command(BaseCommand):
    help = 'Generate 100 random students'

    def handle(self, *args, **options):
        for _ in range(100):
            Group.generate_group()

