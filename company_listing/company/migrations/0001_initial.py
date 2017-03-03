# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('identifier', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('company_category', models.CharField(max_length=100)),
                ('company_subcategory', models.CharField(max_length=100)),
                ('company_type', models.CharField(max_length=100)),
                ('authorized_capital', models.IntegerField()),
                ('paidup_capital', models.IntegerField()),
                ('incorporation_date', models.DateField()),
                ('address_line1', models.CharField(max_length=200, null=True)),
                ('address_line2', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=10)),
                ('full_address', models.CharField(max_length=2000)),
                ('agm_date', models.DateField(null=True)),
                ('balance_sheet_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[(1, 'Active'), (0, 'Inactive')], default='Active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('din', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=20)),
                ('appointment_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
    ]
