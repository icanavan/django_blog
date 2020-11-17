from django.urls import path
from blogging.views import BloggingListView, BloggingDetailView

urlpatterns = [
    path('posts/<int:post_id>/', stub_view, name="blog_detail"),
    path('', BloggingListView.as_view(), name="blog_index"),
    path('posts/<int:post_id>/', BloggingDetailView.as_view(), name="blog_index"),


]