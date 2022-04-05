import datetime
from django.db import models
from decimal import Decimal
from location_field.models.plain import PlainLocationField
from versatileimagefield.fields import VersatileImageField
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from coordinators.utils import generate_password
from core.models import BaseModel,UserLog
from core.utils import EMPLOYEE_TYPE_CHOICE,EMPLOYEE_DESIGNATION_CHOICE,EMPLOYEE_DEPARTMENT_CHOICE
from staffs.models import Staff


TARGET_TYPE_CHOICE = (("PRIMARY", "PRIMARY"), ("SECONDARY", "SECONDARY"))

class GlobalManager(BaseModel):
    staff_type = models.CharField(max_length=128,choices=EMPLOYEE_TYPE_CHOICE,default="permanent")
    department = models.CharField(max_length=128,choices=EMPLOYEE_DEPARTMENT_CHOICE,default="SALES")
    designation = models.CharField(max_length=128,choices=EMPLOYEE_DESIGNATION_CHOICE,default="GM")
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
    user = models.OneToOneField(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not User.objects.filter(username=self.phone).exists():
            password = generate_password()
            user = User.objects.create_user(
                username=self.phone,
                first_name=self.name,
                employe_id=self.employe_id,
                photo=self.photo,
                password=password,
                is_global_manager=True,
                is_staff=False,
                designation=self.designation,
                department=self.department
            )
            self.user = user
            # Creating user logs
            UserLog(
                title="Global manager created",
                description=f'user created with password ## {password} ## and username as @@ {self.phone}'
            ).save()
        else:
            user = User.objects.get(username=self.phone)
            user.first_name = self.name
            user.employe_id = self.employe_id
            user.photo = self.photo
            user.designation=self.designation
            user.department=self.department
            user.save()
        # call the save() method of the parent
        super().save(*args, **kwargs)


""" signal functions for creating Staffs """
@receiver(post_save, sender=GlobalManager)
def create_staff_table(sender, instance, created, **kwargs):
    if not Staff.objects.filter(phone=instance.phone).exists():
        # creating staff model data
        Staff(
            staff_type=instance.staff_type,
            department=instance.department,
            designation=instance.designation,
            employe_id=instance.employe_id,
            name=instance.name,
            email=instance.email,
            phone=instance.phone,
            dob=instance.dob,
            city=instance.city,
            address=instance.address,
            salary=instance.salary,
            location=instance.location,
            photo=instance.photo,
            visa_number=instance.visa_number,
            visa_expiry=instance.visa_expiry,
            passport_number=instance.passport_number,
            passport_expiry=instance.passport_expiry,
            user=instance.user
        ).save()
    else:
        staff = Staff.objects.get(phone=instance.phone)
        staff.staff_type=instance.staff_type,
        staff.department=instance.department,
        staff.designation=instance.designation,
        staff.employe_id=instance.employe_id,
        staff.name=instance.name,
        staff.email=instance.email,
        staff.phone=instance.phone,
        staff.dob=instance.dob,
        staff.city=instance.city,
        staff.address=instance.address,
        staff.salary=instance.salary,
        staff.location=instance.location,
        staff.photo=instance.photo,
        staff.visa_number=instance.visa_number,
        staff.visa_expiry=instance.visa_expiry,
        staff.passport_number=instance.passport_number,
        staff.passport_expiry=instance.passport_expiry,
        staff.save()

""" end signals """

class GlobalManagerTarget(BaseModel):
    YEAR_CHOICES = [(y, y) for y in range(1950, datetime.date.today().year + 2)]
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]

    user = models.ForeignKey(
        GlobalManager, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
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


class GlobalManagerTask(BaseModel):
    task = models.CharField(max_length=350)
    user = models.ForeignKey(
        GlobalManager, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name

