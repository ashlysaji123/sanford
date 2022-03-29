from django.db import models

from core.models import BaseModel
from decimal import Decimal
from products.models import Product
from django.core.validators import MinValueValidator

from versatileimagefield.fields import VersatileImageField



class DARTask(BaseModel):
    executive = models.ForeignKey(
        "executives.SalesExecutive",
        limit_choices_to={"is_deleted": False},
        on_delete=models.CASCADE,
    )
    shop = models.ForeignKey("core.Shop", on_delete=models.CASCADE)
    visit_date = models.DateField("Visiting date")
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    available_time = models.PositiveIntegerField(default=1)
    time_taken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.executive.name} - {self.shop.name}"

    def get_dar_notes(self):
        return DARNotes.objects.filter(dar=self)

class DARNotes(BaseModel):
    DAR_TYPES = (
        ('money','Money Collection'),
        ('order','Collecting Order'),
        ('photo','Uploade Image'),
    )
    dar = models.ForeignKey(
        DARTask, limit_choices_to={"is_deleted": False}, 
        on_delete=models.CASCADE, 
        blank=True, null=True
    )
    note = models.CharField(max_length=221)
    type = models.CharField("Select type of task",max_length=221,choices=DAR_TYPES)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.dar.executive.name)


class DARReschedule(BaseModel):
    dar = models.ForeignKey(
        DARTask, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    reschedule_date = models.DateField("Reschedule date")
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.dar.shop.name)


class CollectMoney(BaseModel):
    total_credit_amount = models.DecimalField(max_digits=10,decimal_places=2)
    received_money = models.DecimalField(max_digits=10,decimal_places=2)
    dar_note = models.ForeignKey(
        DARNotes, limit_choices_to={"is_deleted": False}, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.dar_note.dar.shop.name} - on {self.dar_note.dar.visit_date}"


class Order(BaseModel):
    dar_note = models.ForeignKey(
        DARNotes, limit_choices_to={"is_deleted": False}, 
        on_delete=models.CASCADE
    )
    total_amount = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    advanced_amount =  models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    def __str__(self):
        return f"{self.dar_note.dar.shop.name} - on {self.dar_note.dar.visit_date}"


class OrderItem(BaseModel):
    product =  models.ForeignKey(
        Product,
        limit_choices_to={"is_deleted": False},
        on_delete=models.PROTECT
    )
    qty = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(
        Order, limit_choices_to={"is_deleted": False}, 
        on_delete=models.CASCADE
    )
    total_items_amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.product.name)


class UploadPhoto(BaseModel):
    dar_note = models.ForeignKey(
        DARNotes, limit_choices_to={"is_deleted": False}, 
        on_delete=models.CASCADE
    )
    image1 = VersatileImageField(
        "Image", upload_to="reports/shelfs"
    )
    image2 = VersatileImageField(
        "Image", upload_to="reports/shelfs",
        blank=True,null=True
    )
    image3 = VersatileImageField(
        "Image", upload_to="reports/shelfs",
        blank=True,null=True
    )
    def __str__(self):
        return f"{self.dar_note.dar.shop.name} - on {self.dar_note.dar.visit_date}"