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


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField(unique=True)
    password = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='user/', blank=True, null=True)    
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


# class Review(models.Model):
class Review(models.Model):
    image = models.FileField(
        upload_to="review/", max_length=250, null=True, default=None
    )
    name = models.CharField(max_length=100)
    review = models.TextField()
    stars = models.IntegerField(choices=[(i, f"{i} star") for i in range(1, 6)])

    def __str__(self):
        return f"Review by {self.name}"


class Hotel(models.Model):
    hotel_id = models.CharField(max_length=10, primary_key=True)
    hotel_name = models.CharField(max_length=30)
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


# contact table
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
