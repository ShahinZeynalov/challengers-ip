from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    message_text = forms.CharField(
        label='',
        min_length=50,
        required=True,
        max_length=1000,
        widget = forms.Textarea(
            attrs = {
                'name': 'message_text',
                'cols': '30',
                'rows': '5',
            }
        )
    )
    sender_name = forms.CharField(
        label='',
        min_length=3,
        required=True,
        widget = forms.TextInput(
            attrs = {
            'name': 'sender_name',
            }
        )
    )
    sender_email = forms.CharField(
        label='',
        min_length=10,
        required=True,
        widget = forms.EmailInput(
            attrs = {
            'name': 'sender_email',
            }
        )
    )
    class Meta:
        model = Message
        fields = ('message_text','sender_name','sender_email')
