# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='img',
            field=models.ImageField(null=True, upload_to=b'user_images', blank=True),
        ),
    ]
