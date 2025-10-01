from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView , DetailView, FormView
from .models import Article
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.views import View
from django.views.generic.detail import SingleObjectMixin



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
    

class CommentGet(LoginRequiredMixin, DetailView): # show comment, the client request is to get data
    model = Article
    template_name = 'articles/detail_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = 'articles/detail_article.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        article = self.get_object()
        return reverse("articledetail", kwargs={"pk": article.pk})


class DetailArticle(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


