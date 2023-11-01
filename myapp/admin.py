from django.contrib import admin

# Register your models here.
from .models import Review
from myapp.models import Hotel

admin.site.register(Review)

# admin.site.register(Hotel)
@admin.register(Hotel)
class Hotel(admin.ModelAdmin):
    list_display=('hotel_id','hotel_name','hotel_about','hotel_feature1','hotel_feature2','hotel_feature3','hotel_feature4','hotel_feature5','hotel_image1','hotel_image2','hotel_image3','hotel_image4','hotel_image5')
