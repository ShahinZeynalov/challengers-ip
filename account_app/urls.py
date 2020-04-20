from django.urls import path
from .views import CustomLoginView, UserProfileView, ProfileEditView, ProfileImageEditView
from django.contrib.auth.views import (LogoutView, )

app_name = 'account'

urlpatterns = [
    path('dashboard/settings/profile/', UserProfileView.as_view(), name = 'user-profile'),
    path('dashboard/settings/profile/edit/<int:pk>/', ProfileEditView.as_view(), name = 'user-profile-edit'),
    path('dashboard/settings/profile/edit/picture/<int:pk>/', ProfileImageEditView.as_view(), name = 'user-profile-edit-picture'),
    path('dashboard/settings/admin/', UserProfileView.as_view(), name = 'user-admin'),
    path('dashboard/settings/security/', UserProfileView.as_view(), name = 'user-security'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]
