# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
