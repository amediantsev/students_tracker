import random

from django.db import models
from faker import Faker

fake = Faker()


class Teacher(models.Model):
    DEGREE_CHOICES = [
        ('Master', 'Master'),
        ('Ph.D', 'Ph.D.'),
        ('M.D.', 'M.D.'),
        ('J.D.', 'J.D.'),
    ]

    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    academic_degree = models.CharField(max_length=64, choices=DEGREE_CHOICES,
                                       default=None, null=True, blank=True)
    email = models.EmailField(unique=True)
    # add avatar TODO
    telephone = models.CharField(max_length=64, unique=True)  # clean phone TODO

    def get_info(self):
        return f'{self.first_name}, {self.last_name}, {self.academic_degree}, {self.email}'

    @classmethod
    def generate_teacher(cls):
        teacher = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      email=fake.email(),
                      academic_degree=random.choice(Teacher.DEGREE_CHOICES)[1],
                      telephone=fake.phone_number(),
                      )
        teacher.save()
        return teacher

    def __str__(self):
        return f'{self.academic_degree} {self.first_name} {self.last_name}'


import teachers.signals
