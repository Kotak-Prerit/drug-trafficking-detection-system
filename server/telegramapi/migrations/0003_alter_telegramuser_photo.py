# Generated by Django 5.0.6 on 2024-09-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telegramapi", "0002_telegramuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="telegramuser",
            name="photo",
            field=models.FileField(blank=True, null=True, upload_to="profile_media/"),
        ),
    ]
