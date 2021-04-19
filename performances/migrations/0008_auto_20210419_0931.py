# Generated by Django 3.1.6 on 2021-04-19 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('performances', '0007_auto_20210410_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='group_leader',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='performance_group_leader', to='accounts.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='group_size',
            field=models.CharField(default='Duet', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='institution',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='performances.institution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='members',
            field=models.ManyToManyField(related_name='performance_group_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='performance',
            name='performance_type',
            field=models.CharField(choices=[('INDEPENDENT', 'Independent'), ('DEPENDENT', 'Dependent')], default='Dependent', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='performer_name',
            field=models.CharField(default='Isukuti Dancers', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='sponsor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='performance_sponsor', to=settings.AUTH_USER_MODEL),
        ),
    ]