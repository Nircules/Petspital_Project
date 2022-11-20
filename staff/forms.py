import datetime
from django import forms
from datetime import date
from accounts.models import Assistant, Vet, UserProfile, Pet, Specie, User
from .models import Appointment
from django.core.exceptions import ValidationError

years = [year for year in range(1980, 2023)]


class RegisterPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'owner': forms.HiddenInput(),
            'birth_date': forms.SelectDateWidget(years=years)
        }

    def clean(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date > datetime.date.today():
            raise forms.ValidationError('Invalid Date')


class PatientSearch(forms.Form):
    search_patient = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'list': 'patients'}),
                                     label='Search Patient', error_messages=False)

    def clean(self):
        cleaned_data = super(PatientSearch, self).clean()
        if 'search_patient' in self.errors:
            del self._errors['search_patient']
        return cleaned_data


class CreateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'description', 'appointment_date', 'hour_slot', 'created_by']
        widgets = {
            'pet': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 3}),
            'appointment_date': forms.SelectDateWidget(attrs={'onchange': "showhours()"}),
            'created_by': forms.HiddenInput(),
        }
        labels = {
            'appointment_date': 'Date',
            'appointment_time': 'Hour',
        }

    def clean(self):
        appointment_date = self.cleaned_data.get('appointment_date')
        if appointment_date < date.today():
            raise forms.ValidationError('Invalid Date.')


class UpdateAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['created_by', 'creation_date', 'pet']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'appointment_date': forms.SelectDateWidget(attrs={'onchange': "showhours()"}),
            'results': forms.Textarea(attrs={'rows': 3}),
        }


class ChangeDate(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)
    date.label = ''
