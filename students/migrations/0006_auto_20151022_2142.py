# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20151022_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('faculty', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateField(verbose_name='date created')),
            ],
        ),
        migrations.RemoveField(
            model_name='groupsst',
            name='author',
        ),
        migrations.RemoveField(
            model_name='students',
            name='author',
        ),
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.ForeignKey(to='students.Groups'),
        ),
        migrations.DeleteModel(
            name='GroupsSt',
        ),
    ]
