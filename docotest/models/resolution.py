# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Resolution(models.Model):
    author = models.ForeignKey(User, related_name='resolutions')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        db_table = 'resolution'
        ordering = ['last_modified']
        managed = True
        app_label = 'docotest'

    def __unicode__(self):
        return '{0}'.format(self.description)

    def knockout_fields(self):
        return['description']
