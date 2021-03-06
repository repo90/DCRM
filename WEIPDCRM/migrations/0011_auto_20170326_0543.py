# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0010_auto_20170326_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='copyright_year',
            field=models.PositiveIntegerField(help_text='If input 2016, the final display is \xa9 2016-2017, leave a blank will display the current year.', max_length=255, null=True, verbose_name='Starting Year of Copyright'),
        ),
    ]
