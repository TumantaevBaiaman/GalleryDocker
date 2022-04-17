from django.contrib import admin
from django.urls import path
from .views import (
    ListIMG, ListVideo,
    ListIMGGallery, ListPost,
    DetailPost, ListVideoGallery
)

urlpatterns = [
    path('post/', ListPost.as_view(), name='post'),
    path('post/<int:pk>/', DetailPost.as_view(), name='detail_post'),
    path('create/img/', ListIMG.as_view(), name='create_img'),
    path('create/video/', ListVideo.as_view(), name='create_video'),
    path('gallery/img/', ListIMGGallery.as_view(), name='gallery_img'),
    path('gallery/video', ListVideoGallery.as_view(), name='gallery_video'),
]