from django.db import models
import datetime as dt


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

  
    def __str__(self):
        return self.name
    
    
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='photo/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location) 
    description = models.TextField()

    @classmethod
    def search_by_title(cls,seearch_term):
        return Photo
