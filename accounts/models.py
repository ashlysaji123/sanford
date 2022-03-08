import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg, Sum
from location_field.models.plain import PlainLocationField
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel,Region
from rewards.models import RewardPoint


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )

    is_sales_manager = models.BooleanField(default=False)
    is_sales_coordinator = models.BooleanField(default=False)
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
            null=True
        )

    def __str__(self):
        if self.first_name:
            return str(self.first_name)
        return str(self.username)






class FavouriteGroup(BaseModel):
    user = models.ForeignKey('accounts.User',limit_choices_to={'is_active': True}, on_delete=models.CASCADE)
    group = models.ForeignKey( "products.ProductGroup",limit_choices_to={'is_deleted': False}, related_name="accounts_favourite_group", on_delete=models.CASCADE)
    is_active = models.BooleanField("Mark as Active", default=False)

    def __str__(self):
        return str(self.user)
