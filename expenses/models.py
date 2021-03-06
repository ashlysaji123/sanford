from decimal import Decimal
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models

from core.models import BaseModel


class Expenses(BaseModel):
    user = models.ForeignKey(
        "accounts.User",
        limit_choices_to={"is_active": True},
        on_delete=models.CASCADE,
        default=1,
    )
    date = models.DateField(
        help_text="Date.",
    )
    expense_type = models.CharField(max_length=350)
    amount = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    description = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    # Higher RQ model fields
    coordinator_approved = models.BooleanField(default=False)
    coordinator_rejected = models.BooleanField(default=False)
    supervisor_approved = models.BooleanField(default=False)
    supervisor_rejected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.expense_type} - {self.user}"

