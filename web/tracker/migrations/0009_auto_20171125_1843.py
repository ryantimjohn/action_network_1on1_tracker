# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20171125_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oneonone',
            old_name='other_enpoint',
            new_name='other_endpoint',
        ),
    ]
