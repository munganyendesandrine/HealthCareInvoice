# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_care_invoice_app', '0020_auto_20190417_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetails',
            name='consultation',
            field=models.CharField(default=4, max_length=100),
            preserve_default=False,
        ),
    ]
