from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
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


"""     같은거임
admin 패널에서 이 User를 보고싶다
user를 컨트롤한 클래스가 바로 이거야

class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.User, CustomUserAdmin) 
"""
