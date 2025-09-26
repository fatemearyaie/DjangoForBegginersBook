from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class PostList(ListView):
    model = Posts
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Posts
    template_name = 'detail.html'

class PostCreate(CreateView):
    model = Posts
    template_name = 'create.html'
    fields = ['title', 'body', 'author']

class PostUpdate(UpdateView):
    model = Posts
    template_name = 'edit.html'
    fields = ['title', 'body', 'author']

class PostDelete(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('postlist')