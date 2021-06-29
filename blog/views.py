from django.shortcuts import render
from django.views import generic
from .models import Post

# app_name = 'blog'
# Create your views here.
class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'