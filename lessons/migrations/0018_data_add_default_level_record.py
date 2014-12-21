# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_level_none(apps, schema_editor):
  Level = apps.get_model("lessons", "Level")
  level = Level.objects.create(name = "All levels", position = 0)
  level.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0017_level'),
    ]

    operations = [
      migrations.RunPython(add_level_none)
    ]
