# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20140925_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=200)),
                ('last', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75)),
                ('isLead', models.BooleanField(default=False)),
                ('isFollow', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=True)),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
