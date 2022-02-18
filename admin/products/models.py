# -*- coding: utf-8 -*-

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.title) + "  " + str(self.image)


class User(models.Model):
    pass
