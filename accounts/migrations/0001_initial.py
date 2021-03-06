# Generated by Django 3.1.6 on 2021-03-28 10:15

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=30, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('role', models.CharField(choices=[('TEACHER', 'Teacher'), ('ADJUDICATOR', 'Adjudicator'), ('INDEPENDENT_PERFORMER', 'Independent Performer'), ('DEPENDENT_PERFORMER', 'Dependent Performer'), ('SPONSOR', 'Sponsor'), ('TRAINER', 'Trainer'), ('HEAD_OF_INSTITUTION', 'Head of Institution')], default='TEACHER', max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', accounts.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdjudicatorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'adjudicator',
                'verbose_name_plural': 'adjudicators',
            },
        ),
        migrations.CreateModel(
            name='DependentPerformerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'dependent_performer',
                'verbose_name_plural': 'dependent_performers',
            },
        ),
        migrations.CreateModel(
            name='HeadOfInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='IndependentPerformerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('PAYPAL', 'Paypal'), ('MPESA', 'Mpesa')], default='MPESA', max_length=10)),
            ],
            options={
                'verbose_name': 'independent_performer',
                'verbose_name_plural': 'independent_performers',
            },
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performers', models.ManyToManyField(related_name='performers_under_care', to='accounts.DependentPerformerProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='SponsorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('PAYPAL', 'Paypal'), ('MPESA', 'Mpesa')], default='MPESA', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
            },
        ),
    ]
