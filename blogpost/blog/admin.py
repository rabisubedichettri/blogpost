from django.contrib import admin

# local imports
from .models import Post,Tag,PostTag,PostMeta,Category,PostCategory,PostComment
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(PostComment)
admin.site.register(Category)
admin.site.register(PostCategory)


# changing default django's admin
admin.site.site_header = "BlogPost Admin"
admin.site.site_title = "BlogPost Admin Portal"
admin.site.index_title = "Welcome to BlogPost Admin Portal"
