from django import forms
from .models import User
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.forms import ( AuthenticationForm, PasswordChangeForm )
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='',
        widget = forms.EmailInput(
            attrs={
                'placeholder' : 'Email',
                'class' : 'form-control shadow-none',
                'type': 'email',
            }))
    password = forms.CharField(
        label='',
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Password',
                'class': 'form-control shadow-none',
                'type': 'password',
            }
        )
    )
    class Meta:
        model = User
        fields = ['username','password']


class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'gender']


class ProfileImageEditForm(forms.ModelForm):
    profile_image = forms.ImageField(widget = forms.FileInput(attrs={'class' : 'form-control shadow-none',}))

    class Meta:
        model = User
        fields = ['profile_image']
