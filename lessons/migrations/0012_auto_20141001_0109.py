# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_practice_timing_and_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='timing_and_music',
        ),
        migrations.AddField(
            model_name='practice',
            name='timing_and_music_1',
            field=models.ForeignKey(related_name='timing_1', blank=True, to='lessons.Instructor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='practice',
            name='timing_and_music_2',
            field=models.ForeignKey(related_name='timing_2', blank=True, to='lessons.Instructor', null=True),
            preserve_default=True,
        ),
    ]
