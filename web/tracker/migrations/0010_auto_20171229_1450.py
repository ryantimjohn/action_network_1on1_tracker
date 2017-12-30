# Generated by Django 2.0 on 2017-12-29 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20171125_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oneonone',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.Contact'),
        ),
        migrations.AlterField(
            model_name='oneonone',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
