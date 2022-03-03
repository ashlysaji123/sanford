from django.db import models
from location_field.models.plain import PlainLocationField
from versatileimagefield.fields import VersatileImageField
import datetime

from core.models import BaseModel



TARGET_TYPE_CHOICE = (
        ("PRIMARY", "PRIMARY"),("SECONDARY", "SECONDARY")
    )


class SalesExecutive(BaseModel):
    name = models.CharField(max_length=128)
    employe_id = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=30, blank=True, null=True)
    location = PlainLocationField(based_fields=["city"], zoom=1)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField("User Adress", blank=True, null=True)
    dob = models.DateField("Date of Birth", null=True, blank=True)
    photo = VersatileImageField(
        "User Profile Photo", blank=True, null=True, upload_to="accounts/user/photo/"
    )
    visa_number = models.CharField("Visa Number", max_length=30, blank=True, null=True)
    visa_expiry = models.DateField("Visa Expiry Date Number", blank=True, null=True)
    passport_number = models.CharField("Passport Number", max_length=30, blank=True, null=True)
    passport_expiry = models.DateField("Visa Expiry Date Number", blank=True, null=True)
    region = models.ForeignKey(
        'core.Region', on_delete=models.CASCADE, db_index=True)
    country = models.ForeignKey(
        'core.Country', on_delete=models.CASCADE, db_index=True)
    user = models.OneToOneField(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class SalesExecutiveTarget(BaseModel):
    YEAR_CHOICES = [(y,y) for y in range(1950, datetime.date.today().year+2)]
    MONTH_CHOICE = [(m,m) for m in range(1,13)]

    user = models.ForeignKey(SalesExecutive,limit_choices_to={'is_deleted':False}, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year,)
    month = models.PositiveIntegerField(choices=MONTH_CHOICE, default=datetime.datetime.now().month,)
    target_amount = models.PositiveIntegerField(default=0)
    target_type = models.CharField(max_length=128,choices=TARGET_TYPE_CHOICE)
    current_amount = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(f"{self.month}/{self.year} with {self.target_amount} target to {self.user}")


class SalesExecutiveTask(BaseModel):
    task = models.CharField(max_length=350)
    user = models.ForeignKey(SalesExecutive,limit_choices_to={'is_deleted':False}, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name
