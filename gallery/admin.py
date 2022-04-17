from django.contrib import admin
from .models import (
    Post,
    PostImg, GalleryImg,
    PostVideo, GalleryVideo,
)

admin.site.register(Post)
admin.site.register(PostImg)
admin.site.register(PostVideo)
admin.site.register(GalleryVideo)
admin.site.register(GalleryImg)


# Register your models here.
