# Generated by Django 2.2.9 on 2020-02-03 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('students', '0020_remove_studentuser_repeat_the_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentUser',
        ),
    ]