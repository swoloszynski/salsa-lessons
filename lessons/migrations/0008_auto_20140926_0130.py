# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20140926_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='isFollow',
            new_name='is_follow',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='isLead',
            new_name='is_lead',
        ),
    ]
