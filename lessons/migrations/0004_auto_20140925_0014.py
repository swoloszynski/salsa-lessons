# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20140925_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='location',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
