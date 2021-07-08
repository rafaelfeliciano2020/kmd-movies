# Generated by Django 3.2.2 on 2021-06-07 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_commentmodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodels',
            name='comment_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentmodels',
            name='comment',
            field=models.TextField(),
        ),
    ]