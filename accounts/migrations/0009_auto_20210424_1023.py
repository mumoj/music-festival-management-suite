# Generated by Django 3.1.6 on 2021-04-24 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0009_auto_20210419_1245'),
        ('accounts', '0008_auto_20210420_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='independentperformerprofile',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='independentperformerprofile',
            name='performance_class',
        ),
        migrations.AddField(
            model_name='independentperformerprofile',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='performances.institution'),
        ),
        migrations.AddField(
            model_name='independentperformerprofile',
            name='performances',
            field=models.ManyToManyField(related_name='performing_in', to='performances.Performance'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='performances.institution'),
        ),
    ]