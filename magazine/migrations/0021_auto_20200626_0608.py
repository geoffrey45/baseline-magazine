# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0020_auto_20200626_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazineapimodel',
            name='article_imagee',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
