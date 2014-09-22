# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_charts', '0003_nutritionparameters_nutrition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthparameters',
            name='weight',
            field=models.DecimalField(help_text=b'Can Be Bank: Units lbs', null=b'True', max_digits=5, decimal_places=2),
        ),
    ]
