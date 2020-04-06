from django.shortcuts import render
from django.contrib.auth.views import (LoginView, )
from .forms import LoginForm
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard:dashboard')
