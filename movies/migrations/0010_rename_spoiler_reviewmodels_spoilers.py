# Generated by Django 3.2.2 on 2021-06-07 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_rename_comment_user_commentmodels_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodels',
            old_name='spoiler',
            new_name='spoilers',
        ),
    ]
