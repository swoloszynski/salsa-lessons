# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0013_practice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='status',
            field=models.CharField(default='D', max_length=200, choices=[('S', 'Scheduled'), ('D', 'Draft'), ('P', 'Published')]),
        ),
    ]
