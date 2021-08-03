from os import name
from django.db import models
from django.db.models.base import Model


class StuModel(models.Model):
    """ Students Model Definition """

    stu_name = models.CharField(max_length=40)

    def __str__(self):
        return self.stu_name

    class Meta:
        verbose_name_plural = "STUDENTS"
