from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
# from .models import Review

# admin.site.register(Review)
=======
from .models import *
from myapp.models import Hotel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ["last_login", "created_at", "updated_at"]
    list_display = [
        "name",
        "email",
        "password",
        "picture",
        "is_active",
        "is_admin",
        "is_superuser",
        "created_at",

    ]

    def get_exclude(self, request, obj=None):
        # Exclude the password field from the admin form
        exclude = super().get_exclude(request, obj) or []
        exclude.extend(["password", "user_permissions", "groups"])
        return exclude


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ("image", "name", "review", "stars")


# admin.site.register(Hotel)
@admin.register(Hotel)
class Hotel(admin.ModelAdmin):
    list_display = (
        "hotel_id",
        "hotel_name",
        "hotel_about",
        "hotel_feature1",
        "hotel_feature2",
        "hotel_feature3",
        "hotel_feature4",
        "hotel_feature5",
        "hotel_image1",
        "hotel_image2",
        "hotel_image3",
        "hotel_image4",
        "hotel_image5",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
>>>>>>> f6984537c415d25f98ba1be64cb40c8d8fb1a48f
