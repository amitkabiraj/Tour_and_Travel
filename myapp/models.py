from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    upload_to = "user/"
    ext = filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(upload_to, filename)


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("N", "Not Specified"),
]


# User table
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField(unique=True)
    picture = models.ImageField(upload_to="user/", blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone"]

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user"


# Review Table
# class Review(models.Model):
class Review(models.Model):
    image = models.FileField(
        upload_to="review/", max_length=250, null=True, default=None
    )
    name = models.CharField(max_length=100)
    review = models.TextField()
    stars = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"Review by {self.name}"


#  Hotel table
class Hotel(models.Model):
    hotel_id = models.CharField(max_length=20, primary_key=True)
    hotel_name = models.CharField(max_length=30)
    hotel_price = models.DecimalField(max_digits=10, decimal_places=2)
    allowed_number = models.IntegerField(default=2)
    hotel_dist = models.CharField(max_length=100)
    hotel_about = models.CharField(max_length=50)
    hotel_feature1 = models.CharField(max_length=10)
    hotel_feature2 = models.CharField(max_length=10)
    hotel_feature3 = models.CharField(max_length=10)
    hotel_feature4 = models.CharField(max_length=10)
    hotel_feature5 = models.CharField(max_length=10)
    hotel_image1 = models.FileField(
        upload_to="hotel/", max_length=250, null=True, default=None
    )
    hotel_image2 = models.FileField(
        upload_to="hotel/", max_length=250, null=True, default=None
    )
    hotel_image3 = models.FileField(
        upload_to="hotel/", max_length=250, null=True, default=None
    )
    hotel_image4 = models.FileField(
        upload_to="hotel/", max_length=250, null=True, default=None
    )
    hotel_image5 = models.FileField(
        upload_to="hotel/", max_length=250, null=True, default=None
    )

    def __str__(self):
        return self.hotel_name


# contact table
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"


# Murshidabad place
class place(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    Dist = models.CharField(max_length=100)
    image = models.ImageField(upload_to="place/")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.Dist = self.Dist.capitalize()  # Capitalize the Dist field
        super(place, self).save(*args, **kwargs)


# murshidabad_restaurants


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    Dist = models.CharField(max_length=100)
    restaurant = models.ImageField(upload_to="restaurant_images/")
    menu = models.ImageField(upload_to="restaurant_images/")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.Dist = self.Dist.capitalize()  # Capitalize the Dist field
        super(Restaurants, self).save(*args, **kwargs)


class HotelBooking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, blank=True, null=True)
    aadhaar_no = models.IntegerField(null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    @property
    def total_member(self):
        return self.hotel_booking_members.all().count()

    @property
    def days(self):
        duration = self.check_out - self.check_in
        days = duration.days
        return days

    @property
    def amount(self):
        duration = self.check_out - self.check_in
        days = duration.days
        total_member = self.total_member
        hotel_price = self.hotel.hotel_price
        allowed_number = self.hotel.allowed_number
        total_room = -(-total_member // allowed_number)
        price = hotel_price * total_room
        return price * days

    def __str__(self):
        return f"Booking-id : {str(self.id)}"


class HotelBookingMemberDetail(models.Model):
    hotel_booking = models.ForeignKey(
        HotelBooking,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="hotel_booking_members",
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.name)


CURRENCY_CHOICES = [
    ("INR", "Indian Rupees"),
    ("USD", "US Dollar"),
]


class HotelBookingOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    hotel_booking = models.ForeignKey(
        HotelBooking,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="hotel_booking_orders",
    )
    paid_amount = models.FloatField(null=True, default=0)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default="USD")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    @property
    def rupees(self):
        rupees = self.hotel_booking.amount + 50
        return rupees

    def __str__(self):
        return str(self.hotel_booking)
