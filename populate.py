import os
import django
from accounts.models import Specie
from django.db.utils import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Petspital.settings')
django.setup()


def populate():
    while True:
        try:
            specie = input("Specie Name: ").title()
            new_s = Specie(name=specie)
            new_s.save()
        except IntegrityError:
            print("Already in DB")
            continue
