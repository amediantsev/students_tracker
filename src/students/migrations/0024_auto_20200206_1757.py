# Generated by Django 2.2.9 on 2020-02-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_auto_20200205_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]