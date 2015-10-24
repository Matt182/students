# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20151021_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='created',
            field=models.DateField(verbose_name='date created'),
        ),
    ]
