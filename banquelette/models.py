# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

TYPE_CHOICES = [
        ('card', 'Card')
        ]

CATEGORY_CHOICES = [
        ('courses', 'Courses')
        ]

class Operation(models.Model):
    date = models.DateField()
    op_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    orignale_label = models.CharField(max_length=150)
    custom_label = models.CharField(max_length=150)
    original_amount = models.FloatField()
    custom_amount = models.FloatField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

