from django.contrib import admin
from .models import (
    Post,
    PostImg, GalleryImg,
    PostVideo, GalleryVideo,
    Category, Image
)

admin.site.register(Post)
admin.site.register(PostImg)
admin.site.register(PostVideo)
admin.site.register(GalleryVideo)
admin.site.register(GalleryImg)
admin.site.register(Category)
admin.site.register(Image)


# Register your models here.
