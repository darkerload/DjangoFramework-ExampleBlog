from django.db import models

__author__ = 'abdullah'


class Content(models.Model):
    Head = models.CharField(max_length=100)
    ContentText = models.TextField()


class Comments(models.Model):
    SID = models.IntegerField()
    Message = models.CharField(max_length=250)
