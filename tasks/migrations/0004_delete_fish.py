# Generated by Django 4.1.5 on 2023-01-27 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_rename_perro_fish"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Fish",
        ),
    ]
