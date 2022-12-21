from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Pet, Assistant, Vet
from .forms import ProfileForm, UserCreateForm
from staff.models import Appointment


# Create your views here.
# Register view, if the request.is_staff it won't authenticate, to let the employee keep editing the new patient.
def register(request):
    context = {'form': UserCreationForm}
    if request.method == 'POST':
        form_filled = UserCreationForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            u_username = form_filled.cleaned_data['username']
            u_password = form_filled.cleaned_data['password1']
            user = authenticate(username=u_username, password=u_password)
            if user:
                if 'current_patient' in request:
                    del request.session['current_patient']
                patient = UserProfile.objects.create(user_id=user.id)
                if not request.user.is_staff:
                    login(request, user)
                return redirect('update_profile', patient.id)
            else:
                print("User not authenticated")
        else:
            return render(request, 'register.html', {'form': form_filled})
    return render(request, 'register.html', context)


# The login view.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        u_username = request.POST.get('username')
        u_password = request.POST.get('password')
        user = authenticate(username=u_username, password=u_password)
        if user:
            login(request, user)
            return redirect('homepage')
        else:
            context = {'form': AuthenticationForm(request.POST)}
            messages.add_message(request, messages.WARNING,
                                 "Username and password don't match!")
            return render(request, 'login.html', context)

    else:
        context = {'form': AuthenticationForm}
        return render(request, 'login.html', context)


def user_logout(request):
    request.session['current_patient'] = ''
    logout(request)
    return redirect('login')


# If the request.is_staff then it will update which ever patient he is taking care of now.
# Else the patient can upadte his own details.
@login_required(login_url='login')
def update_profile(request, patient_id):
    user_profile = UserProfile.objects.get(pk=patient_id)
    form = ProfileForm(request.POST or None, instance=user_profile)
    context = {'form': form, 'user_profile': user_profile}
    if form.is_valid():
        form.save()
        request.session['current_patient'] = user_profile.id
        if "assistant" in request.POST:
            new_assistant = Assistant(user_profile=user_profile)
            new_assistant.save()
            user_profile.user.is_staff = True
            user_profile.user.save()
        if "vet" in request.POST:
            new_vet = Vet(user_profile=user_profile)
            new_vet.save()
            user_profile.user.is_staff = True
            user_profile.user.save()
        return redirect('profile', patient_id)

    return render(request, 'update_profile.html', context)


# This view will show the patient's profile.
# It will show his pets where he can make appointment for them or see their details and recent appointments.
@login_required(login_url='login')
def profile(request, patient_id):
    user_profile = UserProfile.objects.get(pk=patient_id)
    pets = Pet.objects.filter(owner=user_profile.id)
    context = {'profile': user_profile, 'pets': pets}
    appointments = Appointment.objects.filter(
        pet__in=pets).order_by('appointment_date', 'hour_slot')
    context['appointments'] = appointments

    return render(request, 'profile.html', context)
