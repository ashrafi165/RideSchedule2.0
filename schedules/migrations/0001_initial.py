# Generated by Django 5.1.2 on 2024-12-02 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Schedule",
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
                ("driver_id", models.CharField(blank=True, max_length=20, null=True)),
                ("pickUp_time", models.CharField(max_length=10)),
                ("pickup_from", models.CharField(max_length=50)),
                ("drop_to", models.CharField(max_length=50)),
                ("pending", models.BooleanField(default=True)),
                (
                    "type_of_schedule",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("daily", "daily"),
                            ("weekly", "weekly"),
                            ("monthly", "monthly"),
                            ("custom", "custom"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("price", models.IntegerField(blank=True, null=True)),
                ("startDate", models.DateField(blank=True, null=True)),
                ("endDate", models.DateField(blank=True, null=True)),
                ("weeks", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "rider_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.profile",
                    ),
                ),
            ],
        ),
    ]
