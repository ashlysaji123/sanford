# Generated by Django 4.0.1 on 2022-03-09 05:10

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Expenses",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        blank=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                (
                    "is_deleted",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")],
                        default=False,
                        verbose_name="Mark as Deleted",
                    ),
                ),
                ("date", models.DateField(help_text="Date.")),
                ("expense_type", models.CharField(max_length=350)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_approved", models.BooleanField(default=False)),
                ("is_rejected", models.BooleanField(default=False)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"is_active": True},
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator_%(class)s_objects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        limit_choices_to={"is_active": True},
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
