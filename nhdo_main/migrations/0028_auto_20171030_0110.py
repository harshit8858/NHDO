# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhdo_main', '0027_remove_profile_level1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
