# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='action_network_id',
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='action_network_id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Organizer'),
        ),
    ]
