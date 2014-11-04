# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0014_auto_20141003_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practice',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='teaches',
            options={'ordering': ['hour'], 'verbose_name': 'assignment'},
        ),
        migrations.AddField(
            model_name='teaches',
            name='additional_instructor',
            field=models.ForeignKey(related_name='teaches_additional', blank=True, to='lessons.Instructor', null=True),
            preserve_default=True,
        ),
    ]
