# Generated by Django 3.1.6 on 2021-05-31 02:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0013_theater_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]