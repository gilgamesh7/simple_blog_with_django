from django.urls import path
from blog.views import AddPostView, HomeView, ArticleDetailView, AddPostView

app_name = "blog"

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('addpost',AddPostView.as_view(), name='add-post'),
]
