# Generated by Django 4.1 on 2022-11-11 22:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_alter_pet_breed"),
        ("staff", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("appointment_date", models.DateTimeField()),
                ("completed", models.BooleanField(default=False)),
                ("results", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "creation_date",
                    models.DateTimeField(
                        default=datetime.datetime(2022, 11, 12, 0, 1, 14, 49783)
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.assistant",
                    ),
                ),
                (
                    "pet",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointments",
                        to="accounts.pet",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Apointment",
        ),
    ]