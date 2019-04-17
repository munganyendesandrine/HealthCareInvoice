# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_care_invoice_app', '0018_auto_20190417_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('household_ID', models.CharField(max_length=16)),
                ('application_ID', models.CharField(max_length=8)),
                ('household_Name', models.CharField(max_length=50)),
                ('ubudehe_Category', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('beneficiary_Name', models.CharField(max_length=50)),
                ('phone_Number', models.CharField(max_length=60)),
                ('sex', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('prisonner', models.CharField(max_length=3)),
                ('catchement_Area', models.CharField(max_length=60)),
            ],
        ),
        migrations.RenameField(
            model_name='healthpost',
            old_name='national_Id',
            new_name='national_ID',
        ),
        migrations.AlterField(
            model_name='healthpost',
            name='health_Post_Name',
            field=models.CharField(max_length=50),
        ),
    ]