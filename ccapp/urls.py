from django.urls import path
from .views import HomePageView, StudentAPIView, chart

app_name = 'challengers'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('chart', chart, name='chart'),
    path('api/challengers/<pk>',StudentAPIView.as_view(), )
]
