from django.db import models


# Create your models here.
class Category(models.Model):
  
    def __str__(self):
        return self
    
    
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    # gallery_image = models.ImageField(upload_to = 'gallery', default = None)
    descripion = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location) 
