# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 06:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(blank=True, default=b'', max_length=100)),
                ('password', models.CharField(blank=True, default=b'', max_length=100)),
                ('name', models.CharField(blank=True, default=b'', max_length=100)),
                ('email', models.EmailField(blank=True, default=b'', max_length=100)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message=b"Enter country code. Phone number must be entered in the format: '919999999'.", regex=b'^\\+?1?\\d{12}$')])),
                ('city_id', models.CharField(blank=True, default=b'', max_length=15)),
                ('address', models.TextField(blank=True, default=b'')),
                ('token_generated', models.TextField(blank=True, default=b'')),
                ('is_admin', models.CharField(blank=True, default=b'', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
