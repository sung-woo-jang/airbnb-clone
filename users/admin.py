from django.contrib import admin
from . import models

# asd
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
