# Generated by Django 3.2.2 on 2021-05-31 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviemodels_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('review', models.TextField()),
                ('spoiler', models.BooleanField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.moviemodels')),
            ],
        ),
    ]
