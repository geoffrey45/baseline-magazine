# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 02:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0017_auto_20200626_0557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazineapimodel',
            name='editors',
        ),
    ]
