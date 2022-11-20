# Generated by Django 4.1 on 2022-10-17 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_userprofile_id_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="breed",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="pet",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pets",
                to="accounts.userprofile",
            ),
        ),
        migrations.DeleteModel(
            name="Breed",
        ),
    ]
