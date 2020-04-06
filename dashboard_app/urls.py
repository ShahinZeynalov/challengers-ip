from django.urls import path
from .views import DashboardTemplateView

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/',DashboardTemplateView.as_view(),name='dashboard' ),
]
