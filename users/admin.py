from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# admin 패널에서 user를 보고싶다는 뜻
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdata",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
