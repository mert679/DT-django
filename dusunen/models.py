from distutils.command.upload import upload
from enum import auto
from unicodedata import category
from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Author(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Categories(models.Model):
    #category_tag = models.ManyToManyField(Post)
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200,null=True)
    def __str__(self):
        return self.category_name

class Post_Tag(models.Model):
    tag_name = models.CharField(max_length=180,unique=True,null=True)
    def __str__(self):
        return self.tag_name

    

class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    number_of_view = models.BigIntegerField()
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    context = tinymce_models.HTMLField()
    categories = models.ManyToManyField(Categories,related_name="Categories")
    status = models.IntegerField(choices=STATUS,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Post_Tag,related_name="post")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Post_img(models.Model):
    post_img = models.CharField(max_length=200)
    