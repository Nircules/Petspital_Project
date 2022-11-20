from django.db import models
import datetime
from accounts.models import UserProfile, Pet, Assistant, Vet


# This function gives the Appointment model a list of tuple of all the hours anyone can make appointment for.
# The tuple will have the hour slot number, and a string that shows the hour time.
# AKA Business Hours.
def business_hours():
    hours_choices = []
    hours = range(8, 20)
    for hour in hours:
        if hour < 10:
            hour = f'0{str(hour)}'
        for ten_min in range(6):
            if ten_min * 10 == 0:
                ten_min = f'{str(ten_min)}0'
            else:
                ten_min = str(ten_min * 10)
            result = str(hour) + f':{ten_min}'
            hours_choices.append(f'{result}')
    hours_choices = list(enumerate(hours_choices))
    return hours_choices


# Create your models here.
# The appointment model, it holds all the necessary details to make all appointments organized.
class Appointment(models.Model):
    hours_of_the_day = business_hours()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments")
    description = models.TextField(max_length=500, null=True, blank=True)
    appointment_date = models.DateField()
    hour_slot = models.IntegerField(choices=hours_of_the_day, null=True)
    completed = models.BooleanField(default=False)
    results = models.TextField(max_length=500, null=True, blank=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(default=datetime.datetime.now())

    @property
    def appointment_hour(self):
        return self.hours_of_the_day[self.hour_slot][1]

    def __str__(self):
        return f"Appointment for - {self.pet.name} ({self.pet.owner}), on " \
               f"{self.appointment_date.__format__('%d/%m/%Y')} at " \
               f"{self.hours_of_the_day[self.hour_slot][1]}"
