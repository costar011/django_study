from django.contrib import admin
from . import models


@admin.register(models.StuModel)
class StuModel(admin.ModelAdmin):
    pass


@admin.register(models.StuMemberModel)
class StuMemberModel(admin.ModelAdmin):
    """ StuMember Model Definition """

    list_stu = (
        "name",
        "gender",
        "view_mobile",
        "email",
    )

    list_gender = ("gender",)
