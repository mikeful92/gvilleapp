# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utility', '0004_auto_20150517_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumption',
            name='Charge',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='consumption',
            name='KWH_Consumption',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
