# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20171125_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oneonone',
            name='contact',
        ),
        migrations.AddField(
            model_name='oneonone',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Contact'),
        ),
    ]
