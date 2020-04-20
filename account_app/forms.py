from django import forms
from .models import User
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.forms import ( AuthenticationForm, )
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

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class ProfileImageEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']
