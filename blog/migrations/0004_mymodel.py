# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170803_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfield', markdownx.models.MarkdownxField()),
            ],
        ),
    ]
