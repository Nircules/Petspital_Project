from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from datetime import timedelta, date, datetime


def is_number(number):
    if not number.isdigit():
        raise ValidationError('ID can contain only numbers.')


# Create your models here.
# This class holds the information of all the users in the App, wether staff or not.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, validators=[
                                 MinLengthValidator(2)])
    email = models.EmailField(unique=True, null=True)
    phone_number = PhoneNumberField(region='IL', unique=True, null=True)
    id_number = models.CharField(unique=True, max_length=9, null=True,
                                 validators=[MinLengthValidator(9), MaxLengthValidator(9), is_number])
    address = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        for field in ['first_name', 'last_name', 'address']:
            value = getattr(self, field)
            if value:
                setattr(self, field, value.title())
        for field in ['email', 'phone_number', 'id_number']:
            value = getattr(self, field)
            if not value:
                setattr(self, field, None)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Class for the Vet employees
class Vet(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=7, decimal_places=2, default=14000)
    is_surgeon = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_profile.first_name} {self.user_profile.last_name}"


# Class for the assistant employees
class Assistant(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=7, decimal_places=2, default=9000)

    def __str__(self):
        return f"{self.user_profile.first_name} {self.user_profile.last_name}"


class Specie(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# The pet class
class Pet(models.Model):
    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=50)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField()
    weight = models.DecimalField(max_digits=4, decimal_places=2)

    @property
    def age(self):
        days = int((datetime.now().date() - self.birth_date).days)
        years = days // 365
        months = (days - years * 365) // 30
        return f"{years}.{months}"

    def __str__(self):
        return f"""
        Name: {self.name}
        Specie: {self.specie}
        Age: {self.birth_date}
        """
