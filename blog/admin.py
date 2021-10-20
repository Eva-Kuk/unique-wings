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
    """ Creates the admin interface for Blog Comment """

    list_display = (
        'comment',
        'blogpost',
        'user_comment'
    )


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
