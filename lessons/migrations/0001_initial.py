# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('style', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('overview', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=700)),
                ('lessons', models.ManyToManyField(to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
