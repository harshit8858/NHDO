# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhdo_main', '0019_auto_20171014_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
