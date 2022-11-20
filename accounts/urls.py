from django.urls import path
from django.contrib.auth import login
from .views import (register, user_login, user_logout, update_profile, profile)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('update_profile/<int:patient_id>', update_profile, name='update_profile'),
    path('profile/<int:patient_id>', profile, name='profile'),
]
