from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserCreateForm(UserCreationForm):
    def __init__(self):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
