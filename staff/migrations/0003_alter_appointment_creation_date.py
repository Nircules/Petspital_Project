# Generated by Django 4.1 on 2022-11-11 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0002_appointment_delete_apointment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="creation_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 11, 22, 10, 4, 136064, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
