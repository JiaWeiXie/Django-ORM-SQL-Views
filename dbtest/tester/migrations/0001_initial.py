# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViewerProduct',
            fields=[
                ('proNo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('proName', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BuyItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('itemNo', models.CharField(max_length=4)),
            ],
        ),
    ]
