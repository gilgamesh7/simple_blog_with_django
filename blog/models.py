from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        # return reverse('blog:article-detail', args=(str(self.id)))
        return reverse('blog:home')
