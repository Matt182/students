# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_newstudents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstudents',
            name='group',
        ),
        migrations.DeleteModel(
            name='NewStudents',
        ),
    ]
