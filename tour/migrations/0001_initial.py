# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]