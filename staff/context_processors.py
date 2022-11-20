from accounts.models import UserProfile
from .forms import PatientSearch
from django.shortcuts import redirect, render


def all_patients(request):
    if request.user.is_staff:
        patients = UserProfile.objects.all()
        return {'patients': patients}
    else:
        return {}


def current(request):
    context = {}
    if request.user.is_staff:
        if "change_current" in request.POST and 'current_patient' in request.session:
            del request.session['current_patient']
        try:
            current_patient = UserProfile.objects.get(pk=request.session['current_patient'])
            context['current_patient'] = current_patient
        except KeyError:
            context = {}
            search_form = PatientSearch(request.POST)
            context['search_form'] = search_form
            if search_form.is_valid() and search_form.cleaned_data:
                current_patient = UserProfile.objects.get(id_number=search_form.cleaned_data['search_patient'])
                request.session['current_patient'] = current_patient.id
                context['current_patient'] = current_patient
        return context
    else:
        return context
