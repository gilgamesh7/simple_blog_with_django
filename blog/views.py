from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Post
from blog.forms import PostForm, UpdateForm

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/update_post.html'
    # fields = ['title', 'title_tag','body']