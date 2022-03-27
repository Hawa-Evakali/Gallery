from django.contrib import admin
from .models import Location, Image, Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category','location')

# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)