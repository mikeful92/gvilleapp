# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ServiceAddress', models.CharField(max_length=120)),
                ('Month', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=4)),
                ('KWH_Consumption', models.IntegerField()),
            ],
        ),
    ]
