from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # 이 폴더에 modelsl.py 를 연결하고


@admin.register(models.User)  # 이 패널에서 User를 보고싶어 라는 뜻~~
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
