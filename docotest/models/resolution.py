# -*- coding: utf-8 -*-
from django.db import models


class Resolution(models.Model):
    author = models.ForeignKey('django.contrib.auth.models', related_name='resolutions')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resolution'
        managed = True
