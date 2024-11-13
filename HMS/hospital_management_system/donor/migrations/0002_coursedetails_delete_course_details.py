# Generated by Django 5.0 on 2024-11-11 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseDetails",
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
                ("course", models.CharField(max_length=100)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="donor.student"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Course_details",
        ),
    ]
