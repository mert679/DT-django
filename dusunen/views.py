from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers,CategorySerializers,TagSerializer
# Create your views here.

@api_view(["GET"])
def posts(request):
    post = Post.objects.filter(status=1).order_by('-created_at')
    serializer = PostSerializers(post,many = True)
    return Response(serializer.data)

@api_view(["GET"])
def tag(request,tag_name=None):
    tag = Post_Tag.objects.filter(tag_name=tag_name).order_by('-tag_name')
    serializer = TagSerializer(tag,many = True)
    return Response(serializer.data)


@api_view(["GET"])
def category(request,slug):
    category = Categories.objects.filter(slug=slug).order_by('-category_name')
    serializer = CategorySerializers(category,many = True)
    return Response(serializer.data)

@api_view(["GET"])
def post_detail(request,slug):
    post_detail = Post.objects.get(slug=slug)
    serializer = PostSerializers(post_detail,many=False)
    return Response(serializer.data)
