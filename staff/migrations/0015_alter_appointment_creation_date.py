# Generated by Django 4.1 on 2022-12-21 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0014_alter_appointment_creation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="creation_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 21, 18, 42, 33, 121964)
            ),
        ),
    ]
