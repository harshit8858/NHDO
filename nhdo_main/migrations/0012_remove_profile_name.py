# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhdo_main', '0011_yourreferal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
