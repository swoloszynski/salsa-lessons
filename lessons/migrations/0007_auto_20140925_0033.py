# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_auto_20140925_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
