# Generated by Django 3.1.6 on 2021-04-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0009_auto_20210419_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='performance_duration',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
