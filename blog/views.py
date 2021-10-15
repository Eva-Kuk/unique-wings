from django.shortcuts import render

from .models import BlogPost, BlogComment

# Create your views here.


def blog(request):
    """ A view to display all blog posts """

    blogposts = BlogPost.objects.all().order_by("-date_posted")

    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blog/blog.html', context)
