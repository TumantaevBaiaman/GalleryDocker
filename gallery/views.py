from django.contrib.auth.models import User
from django.shortcuts import render
import json

from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, permissions, viewsets, status
from rest_framework.decorators import action, api_view, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .serializers import (
    CreateImageSerializer, CreateVideoSerializer,
    GalleryImageSerializer, GalleryVideoSerializer,
    PostSerializer, PostSerializerList,
    CreateImgSerializer
)
from .models import (
    Post,
    PostImg, PostVideo,
    GalleryVideo, GalleryImg,
)
from .permissions import IsOwner


class ViewSet(viewsets.ModelViewSet):
    """
       A viewset that provides the standard actions
       """
    queryset = PostImg.objects.all()
    serializer_class = CreateImageSerializer


class ListIMG(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    serializer_class = CreateImageSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = PostImg.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class ListVideo(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    serializer_class = CreateVideoSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = PostVideo.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class ListIMGGallery(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    serializer_class = GalleryImageSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = GalleryImg.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class ListVideoGallery(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    serializer_class = GalleryVideoSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = GalleryVideo.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class ListPost(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = PostSerializerList
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Post.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailPost(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)

