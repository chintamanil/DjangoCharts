# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_charts', '0004_auto_20140922_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessparameters',
            name='fitness_day',
            field=models.CharField(help_text=b'Day', max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='healthparameters',
            name='health_day',
            field=models.CharField(help_text=b'Day', max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nutritionparameters',
            name='nutrition_day',
            field=models.CharField(help_text=b'Day', max_length=10, null=True),
            preserve_default=True,
        ),
    ]
