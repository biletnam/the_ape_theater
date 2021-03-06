# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-06 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180222_1145'),
        ('accounts', '0009_classmember_purchase_date'),
        ('classes', '0007_auto_20180402_1239'),
        ('square_payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeatReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='accounts.UserProfile')),
                ('reserved_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.ApeClass')),
                ('reserved_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]
