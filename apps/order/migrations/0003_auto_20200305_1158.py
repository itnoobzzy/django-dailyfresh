# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-03-05 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20171113_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='comment',
            field=models.CharField(default='', max_length=256, verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_no',
            field=models.CharField(default='', max_length=128, verbose_name='支付编号'),
        ),
    ]
