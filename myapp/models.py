from django.db import models

# Create your models here.
# class Review(models.Model):
class Review(models.Model):
    image = models.URLField()
    name = models.CharField(max_length=100)
    review = models.TextField()
    stars = models.IntegerField(choices=[(i, f"{i} star") for i in range(1, 6)])

    def __str__(self):
        return f"Review by {self.name}"
