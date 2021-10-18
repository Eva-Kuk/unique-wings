from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import BlogForm
from .models import BlogPost, BlogComment

# Create your views here.


def blog(request):
    """ A view to display all blog posts """

    blogposts = BlogPost.objects.all().order_by("-date_posted")

    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blogpost_id):
    """ A view to display blog detail page """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    comments = BlogComment.objects.filter(blogpost=blogpost)

    context = {
        'blogpost': blogpost,
        'comments': comments,
    }

    return render(request, 'blog/blog_detail.html', context)


def add_blogpost(request):
    """ A view to Add Blogpost form for admin only """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(
                        request,
                        'Failed to add blog post.\
                        Please ensure the form is valid.')
    else:
        form = BlogForm()
    template = 'blog/add_blogpost.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_blogpost(request, blogpost_id):
    """ A view to Edit Blogpost form for admin only """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(
                    request,
                    'Failed to update the blog post.\
                    Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blogpost)
        messages.info(request, f'You are editing {blogpost.title}')

    template = 'blog/edit_blogpost.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


def delete_blogpost(request, blogpost_id):
    """ A view to Delete Blogpost form for admin only """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user == blogpost.author or request.user.is_superuser:
        blogpost.delete()
        return redirect(reverse('blog'))
    else:
        messages.error(request, 'You cannot do that !')
        return redirect(reverse('blog'))
