from django.urls import path, include

app_name = "v1"
urlpatterns = [
    path("blog/", include("api.v1.blog.urls", namespace="blog")),
]
