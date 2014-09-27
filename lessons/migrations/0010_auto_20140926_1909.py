# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_auto_20140926_0132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teaches',
            options={'verbose_name': 'assignment'},
        ),
        migrations.AddField(
            model_name='teaches',
            name='hour',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
