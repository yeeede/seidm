# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Station(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    s_number = models.CharField(max_length=8)
    name = models.CharField(max_length=32)
    height = models.DecimalField(max_digits=7, decimal_places=4)
    longtitude = models.DecimalField(max_digits=7, decimal_places=4)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
	
