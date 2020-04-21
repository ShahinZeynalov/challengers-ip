from django.shortcuts import render
from django.contrib.auth.views import (LoginView, )
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileEditForm, ProfileImageEditForm
from .models import User
from .forms import LoginForm
from django.urls import reverse_lazy
from .mixins import ProfileEditMixin

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard:dashboard')

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user-profile.html'
    slug_field = 'username'

    def get_object(self,*args,**kwargs):
        object = self.model.objects.get(email=self.request.user)
        return object

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(email = self.request.user)
        context['EditProfileForm'] = ProfileEditForm(instance=self.object)
        context['EditProfileImageForm'] = ProfileImageEditForm(instance=self.object)
        return context

class ProfileEditView(LoginRequiredMixin, ProfileEditMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    fields = ("image",)
    def get_success_url(self):
        return reverse_lazy('account:user-profile')

class ProfileImageEditView(LoginRequiredMixin, ProfileEditMixin, UpdateView):
    model = User
    form_class = ProfileImageEditForm

    def get_success_url(self):
        return reverse_lazy('account:user-profile')
