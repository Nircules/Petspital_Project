# Generated by Django 4.1 on 2022-11-15 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0008_appointment_appointment_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="creation_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 15, 2, 36, 56, 221881)
            ),
        ),
    ]
