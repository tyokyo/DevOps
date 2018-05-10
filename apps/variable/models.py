# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from manager.models import Group
import uuid
__all__ = [
    "Variable", "Var2Group",
]


class Variable(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    key = models.CharField(default='', max_length=30)
    value = models.CharField(default='', max_length=30)

    class Meta:
        ordering = ['id',]
        abstract = True


class Var2Group(Variable):
    group = models.ForeignKey(Group, related_name='vars', default=1)

    class Meta:
        permissions = (('yo_list_var', u'罗列组参数'),
                       ('yo_change_var', u'修改组参数'))

