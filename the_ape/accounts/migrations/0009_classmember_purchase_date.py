# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-21 22:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_ticket_num_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmember',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 3, 21, 22, 52, 50, 676905, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
