from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_Student(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.telephone = ''.join(x for x in instance.telephone if x.isdigit())
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
