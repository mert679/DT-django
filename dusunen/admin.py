from django.contrib import admin
from .models import Post,Post_img,Post_Tag,Author,Categories
# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Post_Tag)
