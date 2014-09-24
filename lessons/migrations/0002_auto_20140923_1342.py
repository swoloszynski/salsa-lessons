# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.CharField(max_length=200)),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
                ('practice', models.ForeignKey(to='lessons.Practice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='practice',
            name='lessons',
        ),
        migrations.AddField(
            model_name='practice',
            name='teachings',
            field=models.ManyToManyField(to='lessons.Lesson', through='lessons.Teaches'),
            preserve_default=True,
        ),
    ]

