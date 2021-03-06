# Generated by Django 3.1.6 on 2021-06-03 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0014_event_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=20)),
                ('sub_county', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='institution',
            name='county',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='region',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='sub_county',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='zone',
        ),
        migrations.AddField(
            model_name='event',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='performances.locality'),
        ),
        migrations.AddField(
            model_name='institution',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='performances.locality'),
        ),
    ]
