from django.core.management.base import BaseCommand
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate 100 random teachers'

    def handle(self, *args, **options):
        for _ in range(100):
            Teacher.generate_teacher()
