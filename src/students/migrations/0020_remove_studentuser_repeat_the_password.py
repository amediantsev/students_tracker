# Generated by Django 2.2.9 on 2020-02-03 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0019_studentuser_repeat_the_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='repeat_the_password',
        ),
    ]
