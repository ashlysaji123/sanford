import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel, Region,UserLog


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )

    designation = models.CharField(max_length=150, blank=True, null=True)
    department = models.CharField(max_length=128,blank=True, null=True)
    is_global_manager = models.BooleanField(default=False)
    is_sales_manager = models.BooleanField(default=False)
    is_sales_coordinator = models.BooleanField(default=False)
    is_sales_supervisor = models.BooleanField(default=False)
    is_sales_executive = models.BooleanField(default=False)
    is_merchandiser = models.BooleanField(default=False)
    employe_id = models.CharField(max_length=128)
    photo = VersatileImageField(
        "User Profile Photo", blank=True, null=True, upload_to="accounts/user/photo/"
    )
    region = models.ForeignKey(
        Region,
        limit_choices_to={"is_deleted": False},
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        if self.first_name:
            return str(self.first_name)
        return str(self.username)
