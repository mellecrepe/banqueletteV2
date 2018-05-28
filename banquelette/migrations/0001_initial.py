# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-18 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('op_type', models.CharField(choices=[('card', 'Card')], max_length=50)),
                ('orignale_label', models.CharField(max_length=150)),
                ('custom_label', models.CharField(max_length=150)),
                ('original_amount', models.FloatField()),
                ('custom_amount', models.FloatField()),
                ('category', models.CharField(choices=[('courses', 'Courses')], max_length=50)),
            ],
        ),
    ]