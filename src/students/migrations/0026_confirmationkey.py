# Generated by Django 2.2.9 on 2020-02-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0025_auto_20200206_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=255)),
                ('key', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
