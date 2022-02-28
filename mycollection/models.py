from django.db import models

# Category Model
class Category(models.Model):
    image_category = models.CharField(max_length=50)

    def __str__(self):
        return self.image_category

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

# Location Model
class Location(models.Model):
    image_location = models.CharField(max_length=50)

    def __str__(self):
        return self.image_location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations


# image model
class Image(models.Model):
    image = models.ImageField(upload_to = "images/")
    image_name = models.CharField(max_length=50)
    image_description = models.TextField(max_length=1000)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    class Meta:
        ordering = ['date']

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains = category)
        return images

