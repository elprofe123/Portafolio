# Generated by Django 5.1.2 on 2025-04-06 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portafolio", "0005_alter_proyect_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Proyect",
            new_name="Project",
        ),
    ]
