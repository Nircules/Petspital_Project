from django.contrib import admin
from .models import UserProfile, Vet, Assistant, Pet

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Vet)
admin.site.register(Assistant)
admin.site.register(Pet)
