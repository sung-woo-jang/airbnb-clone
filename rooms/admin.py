from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        print(obj.rooms.count())
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price",)},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book",)},),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)},),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules",),
            },
        ),
        ("Last Details", {"fields": ("host",)},),
    )

    ordering = ("name", "price")

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    list_filter = (
        "instant_book",
        "host__superhost",  # <- = relationship에 접근
        "host__gender",  # <- =  할 수 있다는 것을 보여주기 위함
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = (
        "=city",
        "^host__username",
    )
    # ManyToManyField 모델만 작동함
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()
        # obj == 객실 (기억(?)해두기)

        """
        어드민 클래스 안의 함수는 self(admin class=RoomAdmin)를 받고
        그리고 object를 받음(현재 object = row)
        """

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmon(admin.ModelAdmin):

    """ """

    pass
