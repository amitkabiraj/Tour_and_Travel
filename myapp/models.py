from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_id=models.CharField(max_length=10,primary_key=True)
    hotel_name=models.CharField(max_length=30)
    hotel_about=models.CharField(max_length=50)
    hotel_feature1=models.CharField(max_length=10)
    hotel_feature2=models.CharField(max_length=10)
    hotel_feature3=models.CharField(max_length=10)
    hotel_feature4=models.CharField(max_length=10)
    hotel_feature5=models.CharField(max_length=10)
    hotel_image1=models.FileField(upload_to="hotel/",max_length=250,null=True,default=None)
    hotel_image2=models.FileField(upload_to="hotel/",max_length=250,null=True,default=None)
    hotel_image3=models.FileField(upload_to="hotel/",max_length=250,null=True,default=None)
    hotel_image4=models.FileField(upload_to="hotel/",max_length=250,null=True,default=None)
    hotel_image5=models.FileField(upload_to="hotel/",max_length=250,null=True,default=None)
