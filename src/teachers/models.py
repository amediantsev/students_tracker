import random

from django.db import models
from faker import Faker

fake = Faker()
degrees = ['Master', 'Ph.D', 'M.D.', 'J.D']


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    academic_degree = models.CharField(max_length=64)
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=64)  # clean phone TODO

    def get_info(self):
        return f'{self.first_name}, {self.last_name}, {self.academic_degree}, {self.email}'

    @classmethod
    def generate_teacher(cls):
        teacher = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      academic_degree=random.choice(degrees),
                      email=fake.email(),
                      telephone=fake.phone_number(),
                      )
        teacher.save()
        return teacher

    def __str__(self):
        return f'{self.academic_degree} {self.first_name} {self.last_name}'
