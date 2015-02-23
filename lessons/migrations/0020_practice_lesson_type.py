# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0019_lesson_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='practice_type',
            field=models.CharField(default='MP', max_length=200, choices=[('MP', 'Monday Practice'), ('OH', 'Office Hours'), ('GL', 'Guest Lesson'), ('O', 'Other')]),
            preserve_default=True,
        ),
    ]
