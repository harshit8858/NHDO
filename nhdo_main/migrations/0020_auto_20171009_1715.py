# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 11:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nhdo_main', '0019_auto_20171009_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='your',
        ),
        migrations.AddField(
            model_name='profile',
            name='your',
            field=models.ManyToManyField(blank=True, null=True, related_name='your_team', to=settings.AUTH_USER_MODEL),
        ),
    ]
