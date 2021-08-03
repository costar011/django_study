from django.contrib import admin
from . import models


@admin.register(models.StuModel)
class StuModel(admin.ModelAdmin):
    pass
