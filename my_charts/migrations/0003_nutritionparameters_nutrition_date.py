# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_charts', '0002_auto_20140922_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionparameters',
            name='nutrition_date',
            field=models.DateField(help_text=b'Date Created', null=True),
            preserve_default=True,
        ),
    ]
