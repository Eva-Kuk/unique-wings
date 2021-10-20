from django.urls import path
from . import views

urlpatterns = [
     path(
          'blog/',
          views.blog,
          name='blog'),
     path(
          '<int:blogpost_id>/',
          views.blog_detail,
          name='blog_detail'),
     path(
          'add/',
          views.add_blogpost,
          name='add_blogpost'),
     path(
          'edit_blogpost/<int:blogpost_id>/',
          views.edit_blogpost,
          name='edit_blogpost'),
     path(
          'delete_blogpost/<int:blogpost_id>/',
          views.delete_blogpost,
          name='delete_blogpost'),
     path(
          'comment/<int:blogpost_id>/',
          views.blog_comment,
          name='blog_comment'),
     path(
          'edit_comment/<int:comment_id>/',
          views.edit_comment,
          name='edit_comment'),
]
