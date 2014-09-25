# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20140923_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='level',
            field=models.CharField(blank=True, max_length=200, choices=[('Intro', 'Intro'), ('Beginner', 'Beginner'), ('Accelerated Beginner', 'Accelerated Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='style',
            field=models.CharField(blank=True, max_length=200, choices=[('On1 Salsa', 'On1 Salsa'), ('On2 Salsa', 'On2 Salsa'), ('Bachata', 'Bachata'), ('On2 Cha Cha', 'On2 Cha Cha'), ('Rueda', 'Rueda')]),
        ),
        migrations.AlterField(
            model_name='practice',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='practice',
            name='notes',
            field=models.CharField(max_length=700, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teaches',
            name='notes',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
