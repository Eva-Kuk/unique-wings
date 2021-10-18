from django.contrib import admin
from .models import BlogPost


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'content',
        'date_posted',
    )


admin.site.register(BlogPost, BlogAdmin)
