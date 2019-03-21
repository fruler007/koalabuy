# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-11 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190311_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(db_index=True, default=1, max_length=64, unique=True),
            preserve_default=False,
        ),
    ]