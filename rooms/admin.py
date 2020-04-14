from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "price")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book"),},),
        (
            "Spaces",
            {
                "classes": ("collapse",),
                "fields": ("guests", "beds", "bedrooms", "baths"),
            },
        ),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rule")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")
    # 따로 또 알아보기

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )

    def count_amenities(self, obj):
        return obj.amenities.conut()

    # count_amenities.short_description = "hello sexy!"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
