from django.urls import path
from .views import (register_pet, create_appointment, appointments_in_date, update_appointment, update_pet, pet_details,
                    cancel_appointment)

urlpatterns = [
    path('register_pet', register_pet, name="register_pet"),
    path('create_appointment/<int:pet_id>', create_appointment, name="create_appointment"),
    path('appointments_in_date', appointments_in_date, name="appointments_in_date"),
    path('update_appointment/<int:appointment_id>', update_appointment, name="update_appointment"),
    path('update_pet/<int:pet_id>', update_pet, name='update_pet'),
    path('pet_details/<int:pet_id>', pet_details, name='pet_details'),
    path('cancel_appointment/<int:appointment_id>', cancel_appointment, name="cancel_appointment")
]
