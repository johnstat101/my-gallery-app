from django.db import models

# Category Model
class Category(models.Model):
    image_category = models.CharField(max_length=30)

    def __str__(self):
        return self.image_category

    def save_category(self):
        self.save()

# Location Model
class Location(models.Model):
    image_location = models.CharField(max_length=30)

    def __str__(self):
        return self.image_location

    def save_location(self):
        self.save()


# image model
class Image(models.Model):
    image = models.ImageField(upload_to = "images/")
    image_name = models.CharField(max_length=30)
    image_description = models.TextField(max_length=100)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id = id)
        return image
    
    @classmethod
    def filter_by_location(cls,location):
        image = cls.objects.filter(image_location = location)
        return image
    
    @classmethod
    def search_image(cls,category):
        image = cls.objects.filter(image_category=category)
        return image

