# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('notes', models.TextField()),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
