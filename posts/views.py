from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.urls import reverse_lazy
    
class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    
class PostCreateView(CreateView):
    model = Post
    template_name = "posts/new.html"
    fields = ["title", "subtitle", "body", "author"]

class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/edit.html"
    fields = ["title", "subtitle", "body"]
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy("list")

