import datetime
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db import models
from location_field.models.plain import PlainLocationField
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel
from core.utils import EMPLOYEE_TYPE_CHOICE,EMPLOYEE_DESIGNATION_CHOICE,EMPLOYEE_DEPARTMENT_CHOICE


class Staff(BaseModel):
    company = models.ForeignKey("core.Company", on_delete=models.CASCADE,blank=True,null=True)
    staff_type = models.CharField(max_length=128,choices=EMPLOYEE_TYPE_CHOICE,default="permanent")
    department = models.CharField(max_length=128,choices=EMPLOYEE_DEPARTMENT_CHOICE)
    designation = models.CharField(max_length=128,choices=EMPLOYEE_DESIGNATION_CHOICE)
    employe_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField("Phone Number", max_length=30, unique=True)
    dob = models.DateField("Date of Birth")
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField("User Address", blank=True, null=True)
    salary = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    location = PlainLocationField(based_fields=["city"], zoom=1, blank=True, null=True)
    photo = VersatileImageField(
        "User Profile Photo", blank=True, null=True, upload_to="accounts/user/photo/"
    )
    visa_number = models.CharField("Visa Number", max_length=30, blank=True, null=True)
    visa_expiry = models.DateField("Visa Expiry Date Number", blank=True, null=True)
    passport_number = models.CharField(
        "Passport Number", max_length=30, blank=True, null=True
    )
    passport_expiry = models.DateField("Passport Expiry Date Number", blank=True, null=True)
    region = models.ForeignKey("core.Region", on_delete=models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return str(self.name)
