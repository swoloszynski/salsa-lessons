# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20140923_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teaches',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='teaches',
            name='practice',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='teachings',
        ),
        migrations.DeleteModel(
            name='Teaches',
        ),
        migrations.AddField(
            model_name='practice',
            name='lessons',
            field=models.ManyToManyField(to='lessons.Lesson'),
            preserve_default=True,
        ),
    ]
