# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_care_invoice_app', '0009_auto_20190417_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthpost',
            name='n_id',
            field=models.PositiveIntegerField(),
        ),
    ]
