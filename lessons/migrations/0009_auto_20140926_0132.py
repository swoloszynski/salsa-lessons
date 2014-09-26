# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_auto_20140926_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='is_follow',
            field=models.BooleanField(default=False, verbose_name='follow'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='is_lead',
            field=models.BooleanField(default=False, verbose_name='lead'),
        ),
    ]
