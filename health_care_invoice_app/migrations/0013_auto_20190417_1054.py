# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_care_invoice_app', '0012_auto_20190417_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthpost',
            name='n_id',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
    ]
