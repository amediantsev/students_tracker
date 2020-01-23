from django.core.management.base import BaseCommand
from students.models import Student, Group
import random


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def handle(self, *args, **options):

        for _ in range(100):
            student = Student.generate_student()
            student.group = random.choice(Group.objects.all())
            student.save()
