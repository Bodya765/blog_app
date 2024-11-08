from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, BlogDeleteView, BlogPostCreateView, BlogPostUpdateView

app_name = 'blog_app'

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='all_posts'),
    path('post/<slug:slug>/', BlogDetailView.as_view(), name='post'),
    path('delete_post/<slug:slug>/',BlogDeleteView.as_view(), name='delete_post'),
    path('update_post/<slug:slug>/', BlogPostUpdateView.as_view(), name='update_post'),
    path('create_post/', BlogPostCreateView.as_view(), name='create_post'),

]
