from django.db.models.signals import pre_save
from django.dispatch import receiver

from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def pre_save_teacher(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.telephone = ''.join(x for x in instance.telephone if x.isdigit())
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
