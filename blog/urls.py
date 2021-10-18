from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<int:blogpost_id>/',
         views.blog_detail,
         name='blog_detail'),
    path('add/',
         views.add_blogpost,
         name='add_blogpost'),
]
