# Generated by Django 4.1 on 2022-10-15 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_userprofile_id_number_delete_customer"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userprofile",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="first_name",
            field=models.CharField(
                max_length=50, validators=[django.core.validators.MinLengthValidator(2)]
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(
                max_length=50, validators=[django.core.validators.MinLengthValidator(2)]
            ),
        ),
    ]