# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0018_data_add_default_level_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='level',
            field=models.ForeignKey(default=1, to='lessons.Level'),
            preserve_default=True,
        ),
    ]
