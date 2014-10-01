# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_auto_20141001_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='status',
            field=models.CharField(default='D', max_length=200, choices=[('D', 'Draft'), ('P', 'Published')]),
            preserve_default=True,
        ),
    ]
