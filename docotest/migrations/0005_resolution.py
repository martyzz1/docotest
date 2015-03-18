# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docotest', '0004_auto_20150318_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(related_name='resolutions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['last_modified'],
                'db_table': 'resolution',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
