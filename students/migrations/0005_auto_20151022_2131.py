# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0004_auto_20151022_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupsSt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('faculty', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateField(verbose_name='date created')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.ForeignKey(to='students.GroupsSt'),
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]
