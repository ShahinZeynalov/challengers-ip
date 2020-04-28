from django.urls import path
app_name = 'student'
from .views import sms
urlpatterns = [
    path('sms', sms)
]
