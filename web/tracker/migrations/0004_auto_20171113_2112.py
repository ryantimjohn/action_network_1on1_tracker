# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20171113_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=62, unique=True),
        ),
    ]