from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'