# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], default='Active', max_length=20),
        ),
    ]
