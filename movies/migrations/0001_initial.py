# Generated by Django 3.2.2 on 2021-05-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MovieModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('launch', models.CharField(max_length=255)),
                ('classification', models.IntegerField()),
                ('synopsis', models.TextField()),
                ('genres', models.ManyToManyField(to='movies.GenreModels')),
            ],
        ),
    ]
