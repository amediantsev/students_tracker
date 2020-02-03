from datetime import datetime
import random

from django.db import models
from django.contrib.auth.models import User
from faker import Faker

from teachers.models import Teacher


fake = Faker()
specializations = ['biology', 'physics', 'chemistry', 'mathematics',
                   'psychology', 'linguistics', 'organizations',
                   'computer_science', 'history']


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey('students.Group',
                              related_name='+',
                              null=True, blank=True,
                              on_delete=models.CASCADE)

    def get_info(self):
        return f'{self.first_name}, {self.last_name}, {self.birth_date}'

    @classmethod
    def generate_student(cls):
        student = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=datetime.now().date(),
                      email=fake.email(),
                      telephone=fake.phone_number(),
                      address=fake.address(),
                      )
        student.save()
        return student

    def __str__(self):
        return f'{self.id} {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    SPEC_CHOICES = [
        ('biology', 'biology'),
        ('physics', 'physics'),
        ('chemistry', 'chemistry'),
        ('mathematics', 'mathematics'),
        ('psychology', 'psychology'),
        ('linguistics', 'linguistics'),
        ('organizations', 'organizations'),
        ('computer_science', 'computer_science'),
        ('history', 'history'),
    ]

    name = models.CharField(max_length=64)
    specialization = models.CharField(max_length=64, choices=SPEC_CHOICES,
                                       default=None, null=True, blank=True)
    study_start_year = models.CharField(max_length=4)
    headman = models.ForeignKey('students.Student',
                                related_name='+',
                                null=True, blank=True,
                                on_delete=models.CASCADE)
    curator = models.ForeignKey('teachers.Teacher',
                                related_name='+',
                                null=True, blank=True,
                                on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f'name_{self.__class__.objects.count() + 1}'
        super().save(*args, **kwargs)

    def get_info(self):
        return f'{self.study_start_year}, {self.specialization}'

    @classmethod
    def generate_group(cls):
        group = cls(specialization=random.choice(Group.SPEC_CHOICES)[1],
                    study_start_year=random.randrange(2000, 2019),
                    headman=random.choice(list(Student.objects.all())),
                    curator=random.choice(list(Teacher.objects.all())),
                    )

        group.save()
        return group

    def __str__(self):
        return f'{self.name} {self.specialization} (curator: {self.curator})'


import students.signals
