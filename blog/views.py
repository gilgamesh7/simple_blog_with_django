from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post
from blog.forms import PostForm, UpdateForm

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

    ordering = ['-id']

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

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'   

    success_url = reverse_lazy('blog:home')