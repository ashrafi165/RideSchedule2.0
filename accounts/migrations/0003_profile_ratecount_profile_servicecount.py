# Generated by Django 5.1.2 on 2025-04-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_rate_profile_birthday"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="rateCount",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="serviceCount",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
