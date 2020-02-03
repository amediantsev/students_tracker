from students_tracker.settings import *

CELERY_TASK_ALWAYS_EAGER = True
CELERY_ALWAYS_EAGER = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
