# Generated by Django 3.2.2 on 2021-05-26 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviemodels',
            name='genres',
        ),
    ]