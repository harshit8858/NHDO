# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhdo_main', '0018_auto_20171009_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referral',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='referal_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Referral',
        ),
    ]
