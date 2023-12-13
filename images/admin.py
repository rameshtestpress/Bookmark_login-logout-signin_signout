
from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'display_image', 'created',]
    list_filter = ['created']
    
    def display_image(self, obj):
        return obj.image  

    display_image.short_description = 'Image'

# Register your models here.
