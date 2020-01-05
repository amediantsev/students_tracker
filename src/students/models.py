from datetime import datetime
from django.db import models
from faker import Faker

fake = Faker()

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16) # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

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

class Group(models.Model):
    specialization = models.CharField(max_length=64)
    study_start_year = models.CharField(max_length=4)
    unique_code = models.CharField(max_length=10)
    quantity_of_students = models.CharField(max_length=3)       # в будущем будет высчитываться автоматически