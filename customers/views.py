from django.shortcuts import render
from accounts.models import UserProfile
from staff.forms import PatientSearch
from django.template import RequestContext
from django.views.defaults import page_not_found


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {})


def about(request):
    return render(request, 'about.html', {})


def clinic(request):
    return render(request, 'clinic.html', {})
