from django.urls import path

from . import views

urlpatterns = [
    path("",views.posts, name="posts"),
    path("detail/<slug:slug>/",views.post_detail, name="post_detail"),
    path("category/<slug:slug/",views.category, name="post_category"),
    path("tag/<slug:tag_name>/",views.tag, name="post_tag")
]
    
