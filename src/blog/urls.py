from django.urls import path

from .views import index, article, blog_list, blog_post

urlpatterns = [
    path('', index, name='blog-index'),
    path('article<str:numero_article>/', article, name='blog-article'),
    path('blog_post<str:numero_post>/', blog_post, name='blog-post'),
    path('blogs_list/', blog_list, name='blog-list'),
]
