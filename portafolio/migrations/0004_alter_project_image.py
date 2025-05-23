# Generated by Django 5.1.2 on 2025-04-28 23:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portafolio", "0003_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                default="https://res.cloudinary.com/tu_cloud_name/image/upload/v12345678/default_image.jpg",
                max_length=255,
                null=True,
                verbose_name="image",
            ),
        ),
    ]
