# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_care_invoice_app', '0017_auto_20190417_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthpost',
            old_name='district_name',
            new_name='district_Name',
        ),
        migrations.RenameField(
            model_name='healthpost',
            old_name='health_facility_type',
            new_name='health_Facility_Type',
        ),
        migrations.RenameField(
            model_name='healthpost',
            old_name='healthpost_name',
            new_name='health_Post_Name',
        ),
        migrations.RenameField(
            model_name='healthpost',
            old_name='national_id',
            new_name='national_Id',
        ),
    ]
