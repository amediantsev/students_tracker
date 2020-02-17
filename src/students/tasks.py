from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from students.models import Logger


@shared_task
def send_email_async(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)


@shared_task
def logger_cleaner():
    now = timezone.now()
    Logger.objects.filter(created__lte=now - timedelta(days=days)).delete()
