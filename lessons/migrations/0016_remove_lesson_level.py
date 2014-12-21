# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0015_auto_20141104_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='level',
        ),
    ]
