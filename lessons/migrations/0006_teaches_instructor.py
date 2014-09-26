# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaches',
            name='instructor',
            field=models.ManyToManyField(to='lessons.Instructor'),
            preserve_default=True,
        ),
    ]
