# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180203_1023'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apeclass',
            name='banner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.BannerWidget'),
        ),
    ]
