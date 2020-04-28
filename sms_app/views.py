from django.shortcuts import render

from .models import Student


def sms(request):
    context = {}
    context['users'] = Student.objects.all()
    return render(request,'sms.html', context)
