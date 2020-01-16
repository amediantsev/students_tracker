from django.core.management.base import BaseCommand
from students.models import Student


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def handle(self, *args, **options):
        for _ in range(100):
            Student.generate_student()
