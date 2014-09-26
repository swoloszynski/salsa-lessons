# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_teaches_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teaches',
            name='instructor',
        ),
        migrations.AddField(
            model_name='teaches',
            name='follow_instructor',
            field=models.ForeignKey(related_name='teaches_follow', blank=True, to='lessons.Instructor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teaches',
            name='lead_instructor',
            field=models.ForeignKey(related_name='teaches_lead', blank=True, to='lessons.Instructor', null=True),
            preserve_default=True,
        ),
    ]
