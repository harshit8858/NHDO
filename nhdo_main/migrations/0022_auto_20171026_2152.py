# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhdo_main', '0021_your_referal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='your_referal',
            old_name='your_referla',
            new_name='your_referal',
        ),
    ]
