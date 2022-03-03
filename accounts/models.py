import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg, Sum
from location_field.models.plain import PlainLocationField
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel
from rewards.models import RewardPoint


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )

    is_sales_manager = models.BooleanField(default=False)
    is_sales_coordinator = models.BooleanField(default=False)
    is_sales_executive = models.BooleanField(default=False)
    is_merchandiser = models.BooleanField(default=False)
    employe_id = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        if self.first_name:
            return str(self.first_name)
        return str(self.username)

    # def get_user_photo(self):
    #     return self.photo.url if self.photo else settings.DEFAULT_AVATAR

    # def get_average_points(self):
    #     average_points = RewardPoint.objects.filter(is_deleted=False, user=self, status="APPROVED").aggregate(Avg('point'))
    #     return (average_points)

    # def get_total_points(self):
    #     total_points = RewardPoint.objects.filter(is_deleted=False, user=self, status="APPROVED").aggregate(Sum('point'))
    #     return (total_points)





class FavouriteGroup(BaseModel):
    user = models.ForeignKey('accounts.User',limit_choices_to={'is_active': True}, on_delete=models.CASCADE)
    group = models.ForeignKey( "products.ProductGroup",limit_choices_to={'is_deleted': False}, related_name="accounts_favourite_group", on_delete=models.CASCADE)
    is_active = models.BooleanField("Mark as Active", default=False)

    def __str__(self):
        return str(self.user)
