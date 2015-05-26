# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utility', '0005_auto_20150519_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ServiceAddress', models.CharField(max_length=120)),
                ('Month', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=4)),
                ('Water_Consumption', models.IntegerField()),
                ('Charge', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Consumption',
            new_name='Electric',
        ),
    ]
