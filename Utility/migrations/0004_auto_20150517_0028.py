# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utility', '0003_consumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='KWH_Consumption',
            field=models.IntegerField(null=True),
        ),
    ]
