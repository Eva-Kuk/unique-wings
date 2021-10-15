from django.contrib import admin
from .models import BlogPost, BlogComment


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'content',
        'date_posted',
    )


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = (
        'user_comment',
        'comment',
        'date',
    )


admin.site.register(BlogPost)
admin.site.register(BlogComment)
