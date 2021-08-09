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


class StuMemberModel(models.Model):
    """ StuMember Model Definition """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    name = models.CharField(max_length=30)
    birth = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    mobile = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def view_mobile(self):
        current_value = self.mobile
        max_len = len(current_value)
        first_mobile = current_value[0:3]
        second_mobile = current_value[3:7]
        third_mobile = current_value[7:max_len]

        return f"{first_mobile}-{second_mobile}-{third_mobile}"

    view_mobile.short_desciprtion = "MOBILE"

    class Meta:
        verbose_name_plural = "STUMEMBER"
