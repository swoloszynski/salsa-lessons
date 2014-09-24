# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20140923_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teaches',
            name='note',
        ),
        migrations.AddField(
            model_name='teaches',
            name='notes',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='notes',
            field=models.CharField(max_length=700, null=True, blank=True),
        ),
    ]
