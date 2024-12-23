# Generated by Django 5.0 on 2024-11-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resource_library", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resource",
            name="category",
            field=models.CharField(
                choices=[
                    ("resume", "Resume Templates"),
                    ("cover_letter", "Cover Letter Templates"),
                    ("guide", "Guides"),
                ],
                default="guide",
                max_length=50,
            ),
        ),
    ]
