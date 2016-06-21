# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 02:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=100)),
                ('shell', models.CharField(choices=[('ZS', 'ZSH'), ('BS', 'BASH')], max_length=2)),
                ('run_time', models.DateTimeField()),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Box')),
            ],
        ),
    ]
