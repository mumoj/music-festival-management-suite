# Generated by Django 3.1.6 on 2021-03-29 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0001_initial'),
        ('accounts', '0002_auto_20210328_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependentperformerprofile',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='performances.institution'),
        ),
        migrations.AlterField(
            model_name='dependentperformerprofile',
            name='performance_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='performances.class'),
        ),
    ]
