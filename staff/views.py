import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.detail import DetailView
from .forms import RegisterPetForm, CreateAppointmentForm, ChangeDate, UpdateAppointment
from accounts.models import Pet
from .models import Appointment
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
# A pet registerion view.
@staff_member_required(login_url='accounts/login')
def register_pet(request):
    try:
        form = RegisterPetForm(request.POST or None, initial={'owner': request.session['current_patient'],
                                                              'birth_date': datetime.date.today()})
        context = {'form': form}
        if form.is_valid() and "pet_register" in request.POST:
            form.save()
            return redirect('homepage')
    except KeyError:
        context = {}

    return render(request, 'pet_register.html', context)


# An update pet view.
# The try block is in case something went wrong with the staff user who holds current_patient attribute.
@staff_member_required(login_url='accounts/login')
def update_pet(request, pet_id):
    try:
        pet = Pet.objects.get(pk=pet_id)
        form = RegisterPetForm(request.POST or None, instance=pet,
                               initial={'owner': request.session['current_patient']})
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('profile', pet.owner.id)
    except KeyError:
        context = {}

    return render(request, 'pet_update.html', context)


# A view that shows the pet's profile, if the request is_staff then he can update the profile
# It also shows all the appointments related to the pet, for the patient to see the clinic results of the appointment.
def pet_details(requets, pet_id):
    pet = Pet.objects.get(pk=pet_id)
    appointments = Appointment.objects.filter(pet=pet)
    context = {'pet': pet, 'appointments': appointments}
    return render(requets, 'pet_details.html', context)


# New Appointment maker. It will filter any unavailable hours for any date.
# This case there can't be any 2 appointments at the same time at the same date.
# Unless the staff changes it in the update method.
def create_appointment(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)
    tomorrow = datetime.date.today() + datetime.timedelta(1)
    form = CreateAppointmentForm(request.POST or None, initial={
        'pet': pet.id,
        'created_by': request.user.user_profile,
        'appointment_date': tomorrow
    })
    appointments = Appointment.objects.filter(completed=False).order_by("appointment_date", "hour_slot")
    business_hours = [hour[1] for hour in Appointment.hours_of_the_day]
    context = {'form': form, 'pet': pet, 'appointments': appointments, 'business_hours': business_hours}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request, 'create_appointment.html', context)


# Only staff can edit the appointment details.
# There they can publish the results of the appointment and mark it as complete.
@staff_member_required(login_url='accounts/login')
def update_appointment(request, appointment_id):
    context = {}
    appointmnet = Appointment.objects.get(pk=appointment_id)
    form = UpdateAppointment(request.POST or None, instance=appointmnet)
    context['form'] = form
    context['appointment'] = appointmnet
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('appointments_in_date')
    return render(request, 'update_appointment.html', context)


# Shows the staff all the appointments for the given date.
# The inital is always today. From the template itself they can change it.
@staff_member_required(login_url='/accounts/login')
def appointments_in_date(request):
    context = {}
    today = datetime.date.today()
    appointments = Appointment.objects.filter(appointment_date=today).order_by('hour_slot')
    form = ChangeDate(request.POST or None, initial={'date': today})
    context['form'] = form
    if appointments:
        context['appointments'] = appointments
    if request.method == "POST":
        if form.is_valid():
            new_date = form.cleaned_data['date']
            context['appointments'] = Appointment.objects.filter(appointment_date=new_date).order_by(
                'hour_slot')
            return render(request, 'show_appointments.html', context)
    return render(request, 'show_appointments.html', context)


# In order to delete an existing appointment it will redirect to another page to make sure.
def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.POST:
        appointment.delete()
        return render(request, "homepage.html", {})
    return render(request, "cancel_appointment.html", {'appointment': appointment})
