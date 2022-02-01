from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True)
    Description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(unique=True, max_length=100, db_index=True)
    meta_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', related_name="parent_category", null=True, blank=True, on_delete=models.SET_NULL)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Tag(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return str(self.id)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_comment', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.post)
