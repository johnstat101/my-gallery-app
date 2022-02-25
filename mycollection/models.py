from email.mime import image
from unicodedata import category
from django.db import models

# Category Model
class Category(models.Model):
    image_category = models.CharField(max_length=30)

# Location Model
class Location(models.Model):
    image_location = models.CharField(max_length=30)


# image model
class Image(models.Model):
    image = models.ImageField(upload_to = "images/")
    image_name = models.CharField(max_length=30)
    image_description = models.TextField(max_length=100)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)

