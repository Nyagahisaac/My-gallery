from django.db import models
import datetime as dt


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
  
    def __str__(self):
        return self
    
    
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField('photo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location) 
    description = models.TextField()

