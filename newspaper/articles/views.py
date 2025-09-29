from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView , DetailView
from .models import Article
from django.urls import reverse_lazy


# Create your views here.
class CreateArticle(CreateView):
    model = Article
    template_name = 'articles/create_article.html'
    fields = ['title', 'body', 'author']