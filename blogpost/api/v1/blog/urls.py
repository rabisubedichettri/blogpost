from django.urls import path
from django.contrib import admin

from .views import PostList, PostDetail
app_name = "blog"
urlpatterns = [
    path('posts/<int:pk>/', PostDetail.as_view(),name="post-detail"),
    path('posts/', PostList.as_view(),name="post-list"),

]
