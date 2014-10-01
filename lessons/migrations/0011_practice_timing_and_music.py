# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_auto_20140926_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='timing_and_music',
            field=models.ForeignKey(blank=True, to='lessons.Instructor', null=True),
            preserve_default=True,
        ),
    ]
