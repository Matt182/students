# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20151022_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupsst',
            name='author',
        ),
    ]
