# Generated by Django 3.1.6 on 2021-05-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0012_auto_20210505_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='name',
            field=models.CharField(default='Auditorium B', max_length=15),
            preserve_default=False,
        ),
    ]
