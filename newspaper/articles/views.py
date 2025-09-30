from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView , DetailView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class CreateArticle(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/create_article.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ListArticle(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/articles_list.html'

class UpdateArticle(LoginRequiredMixin,UserPassesTestMixin , UpdateView):
    model = Article
    template_name = 'articles/edit_article.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class DeleteArticle(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = reverse_lazy('list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class DetailArticle(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/detail_article.html'