# Generated by Django 5.1.2 on 2025-04-03 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portafolio", "0003_alter_proyect_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proyect",
            name="image",
            field=models.ImageField(upload_to="media/portafolio/images"),
        ),
    ]
