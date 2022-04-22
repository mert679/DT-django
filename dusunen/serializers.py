from pyexpat import model
from unicodedata import category
from django.db.models import fields

from rest_framework import serializers
from .models import Post,Author,Categories,Post_Tag



class TagSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug'
    )

    class Meta:
        model = Post_Tag
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = "__all__"

class PostSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = CategorySerializers(many= True, read_only = True)
    class Meta:
        model = Post
        fields ="__all__"
        depth=1

