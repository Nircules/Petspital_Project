# Generated by Django 4.1 on 2022-11-12 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0005_appointment_duration_alter_appointment_creation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="creation_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 12, 15, 12, 58, 229712)
            ),
        ),
    ]
