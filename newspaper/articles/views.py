from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView , DetailView
from .models import Article
from django.urls import reverse_lazy


# Create your views here.
class CreateArticle(CreateView):
    model = Article
    template_name = 'articles/create_article.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ListArticle(ListView):
    model = Article
    template_name = 'articles/articles_list.html'

class UpdateArticle(UpdateView):
    model = Article
    template_name = 'articles/edit_article.html'
    fields = ['title', 'body']

class DeleteArticle(DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = reverse_lazy('list')

class DetailArticle(DetailView):
    model = Article
    template_name = 'articles/detail_article.html'