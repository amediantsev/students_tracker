# Generated by Django 2.2.9 on 2020-01-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_remove_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
