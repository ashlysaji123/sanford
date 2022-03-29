import datetime

from django.db import models
from location_field.models.plain import PlainLocationField
from versatileimagefield.fields import VersatileImageField

from accounts.models import User
from coordinators.utils import generate_password
from core.models import BaseModel

TARGET_TYPE_CHOICE = (("PRIMARY", "PRIMARY"), ("SECONDARY", "SECONDARY"))


class SalesSupervisor(BaseModel):
    name = models.CharField(max_length=128)
    employe_id = models.CharField(max_length=128, unique=True)
    phone = models.CharField("Phone Number", max_length=30, unique=True)
    location = PlainLocationField(based_fields=["city"], zoom=1)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField("User Address", blank=True, null=True)
    dob = models.DateField("Date of Birth")
    photo = VersatileImageField(
        "User Profile Photo", blank=True, null=True, upload_to="accounts/user/photo/"
    )
    visa_number = models.CharField("Visa Number", max_length=30, blank=True, null=True)
    visa_expiry = models.DateField("Visa Expiry Date Number", blank=True, null=True)
    passport_number = models.CharField(
        "Passport Number", max_length=30, blank=True, null=True
    )
    passport_expiry = models.DateField("Passport Expiry Date Number", blank=True, null=True)
    region = models.ForeignKey("core.Region", on_delete=models.CASCADE, db_index=True)
    country = models.ForeignKey("core.Country", on_delete=models.CASCADE, db_index=True)
    user = models.OneToOneField(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # set the value of the read_only_field using the regular field
        if not User.objects.filter(username=self.phone).exists():
            password = generate_password()
            print(password, "mmmmmmmm")
            user = User.objects.create_user(
                username=self.phone,
                first_name=self.name,
                employe_id=self.employe_id,
                photo=self.photo,
                region=self.region,
                password=password,
                is_sales_supervisor=True,
                is_staff=False,
            )
            self.user = user
        else:
            user = User.objects.get(username=self.phone)
            user.first_name = self.name
            user.employe_id = self.employe_id
            user.photo = self.photo
            user.region = self.region
            user.save()
        # call the save() method of the parent
        super().save(*args, **kwargs)


class SalesSupervisorTarget(BaseModel):
    YEAR_CHOICES = [(y, y) for y in range(1950, datetime.date.today().year + 2)]
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]

    user = models.ForeignKey(
        SalesSupervisor, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    year = models.PositiveIntegerField(
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
    )
    month = models.PositiveIntegerField(
        choices=MONTH_CHOICE,
        default=datetime.datetime.now().month,
    )
    target_amount = models.PositiveIntegerField(default=0)
    target_type = models.CharField(max_length=128, choices=TARGET_TYPE_CHOICE)
    current_amount = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(
            f"{self.month}/{self.year} with {self.target_amount} target to {self.user}"
        )

class SalesSupervisorTask(BaseModel):
    task = models.CharField(max_length=350)
    user = models.ForeignKey(
        SalesSupervisor, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name


class SalesExecutive(BaseModel):
    name = models.CharField(max_length=128)
    employe_id = models.CharField(max_length=128, unique=True)
    phone = models.CharField("Phone Number", max_length=30, unique=True)
    location = PlainLocationField(based_fields=["city"], zoom=1)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField("User Address", blank=True, null=True)
    dob = models.DateField("Date of Birth")
    photo = VersatileImageField(
        "User Profile Photo", blank=True, null=True, upload_to="accounts/user/photo/"
    )
    visa_number = models.CharField("Visa Number", max_length=30, blank=True, null=True)
    visa_expiry = models.DateField("Visa Expiry Date Number", blank=True, null=True)
    passport_number = models.CharField(
        "Passport Number", max_length=30, blank=True, null=True
    )
    passport_expiry = models.DateField("Passport Expiry Date Number", blank=True, null=True)
    supervisor = models.ForeignKey(SalesSupervisor, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey("core.Region", on_delete=models.CASCADE, db_index=True)
    country = models.ForeignKey("core.Country", on_delete=models.CASCADE, db_index=True)
    user = models.OneToOneField(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # set the value of the read_only_field using the regular field
        if not User.objects.filter(username=self.phone).exists():
            password = generate_password()
            print(password, "mmmmmmmm")
            user = User.objects.create_user(
                username=self.phone,
                first_name=self.name,
                employe_id=self.employe_id,
                photo=self.photo,
                region=self.region,
                password=password,
                is_sales_executive=True,
                is_staff=False,
            )
            self.user = user
        else:
            user = User.objects.get(username=self.phone)
            user.first_name = self.name
            user.employe_id = self.employe_id
            user.photo = self.photo
            user.region = self.region
            user.save()
        # call the save() method of the parent
        super().save(*args, **kwargs)


class SalesExecutiveTarget(BaseModel):
    YEAR_CHOICES = [(y, y) for y in range(1950, datetime.date.today().year + 2)]
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]

    user = models.ForeignKey(
        SalesExecutive, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    year = models.PositiveIntegerField(
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
    )
    month = models.PositiveIntegerField(
        choices=MONTH_CHOICE,
        default=datetime.datetime.now().month,
    )
    target_amount = models.PositiveIntegerField(default=0)
    target_type = models.CharField(max_length=128, choices=TARGET_TYPE_CHOICE)
    current_amount = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(
            f"{self.month}/{self.year} with {self.target_amount} target to {self.user}"
        )


class SalesExecutiveTask(BaseModel):
    task = models.CharField(max_length=350)
    user = models.ForeignKey(
        SalesExecutive, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name
