from django.contrib import admin

from gallery.models import Category, Location, Photo

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Photo)