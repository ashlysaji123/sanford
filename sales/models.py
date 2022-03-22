from decimal import Decimal
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from core.models import BaseModel


class OpeningStock(BaseModel):
    merchandiser = models.ForeignKey(
        "merchandiser.Merchandiser",
        on_delete=models.CASCADE,
        limit_choices_to={"is_deleted": False},
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        limit_choices_to={"is_deleted": False},
    )
    count = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Opening Stock"
        verbose_name_plural = "Opening Stocks"

    def __str__(self):
        return str(f"{self.merchandiser} - {self.product} with {self.count} stock")


class Sales(BaseModel):
    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    )
    total_amount = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    photo = VersatileImageField(
        "Photo of bill", blank=True, null=True, upload_to="sales/bill/photo/"
    )
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username


class SaleItems(BaseModel):
    sale = models.ForeignKey(
        Sales, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        limit_choices_to={"is_deleted": False},
        on_delete=models.CASCADE,
    )
    qty = models.PositiveIntegerField(default=1)
    total_items_amount = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    def __str__(self):
        if self.sale.user.first_name:
            return self.sale.user.first_name
        else:
            return self.sale.user.username



class SalesApproval(BaseModel):
    sender = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE)
    region = models.ForeignKey(
        "core.Region", on_delete=models.CASCADE)
    manager_approved = models.BooleanField(default=False)
    manager_rejected = models.BooleanField(default=False)
    coordinator_approved = models.BooleanField(default=False)
    coordinator_rejected = models.BooleanField(default=False)
    executive_approved = models.BooleanField(default=False)
    executive_rejected = models.BooleanField(default=False)
    # GENERIC MODELS
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=200)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.sender.first_name)


class SaleReturn(BaseModel):
    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE,blank=True, null=True
    )
    total_amount = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    def __str__(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username
    
    def get_absolute_url(self):
        return reverse("sales:single_sales_return", kwargs={"pk": self.pk})
 


class SaleReturnItems(BaseModel):
    sale = models.ForeignKey(
        SaleReturn, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        limit_choices_to={"is_deleted": False},
        on_delete=models.CASCADE,
    )
    qty = models.PositiveIntegerField(default=1)
    total_items_amount = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    def __str__(self):
        if self.sale.user.first_name:
            return self.sale.user.first_name
        else:
            return self.sale.user.username
