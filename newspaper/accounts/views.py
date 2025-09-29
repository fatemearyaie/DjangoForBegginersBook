from django.shortcuts import render
from django.views.generic import CreateView
from .models import CostumUser
from django.urls import reverse_lazy
from .forms import CostumUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login.html')
    form_class = CostumUserCreationForm
