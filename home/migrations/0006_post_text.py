# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(null=True),
        ),
    ]