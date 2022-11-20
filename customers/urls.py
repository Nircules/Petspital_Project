from django.urls import path
from .views import homepage, clinic, about

urlpatterns = [
    path('', homepage, name="homepage"),
    path('clinic', clinic, name="clinic"),
    path('about', about, name="about"),
]
