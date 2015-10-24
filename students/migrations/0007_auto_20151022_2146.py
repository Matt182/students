# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0006_auto_20151022_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupsSt',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('faculty', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateField(verbose_name='date created')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
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
