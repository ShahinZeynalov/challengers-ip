from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
