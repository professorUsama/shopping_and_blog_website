from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/<int:post_id>", views.blogpost, name="blogpost"),
]