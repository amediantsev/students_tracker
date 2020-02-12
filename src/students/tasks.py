from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from students.models import Logger

@shared_task
def add(a, b):
    print('ADD WORKS!')
    sleep(10)
    print(a + b)
    return a + b


@shared_task
def send_email_async(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)


@shared_task
def logger_cleaner():
    now = timezone.now()
    queryset = Logger.objects.all()
    delete_list = (log for log in queryset if (now - log.created).days > 7)
    for log in delete_list:
        log.delete()
