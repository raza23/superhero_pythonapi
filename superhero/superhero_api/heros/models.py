# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=50)
    identity = models.CharField(max_length=50)
    universe = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name
