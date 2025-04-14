# accounts/urls.py

from django.urls import path
from . import views
from .views import signup_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('signup/', signup_view, name='signup'),

]
