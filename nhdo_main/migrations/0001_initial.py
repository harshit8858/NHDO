# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('query', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referal_id', models.CharField(max_length=10)),
                ('pan_number', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female'), ('OTHER', 'other')], max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(max_length=20)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('full_name', models.CharField(blank=True, max_length=100, verbose_name='full name')),
            ],
            options={
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YourReferal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referal_no', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
