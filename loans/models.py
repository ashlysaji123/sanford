from django.db import models

from core.models import BaseModel
# Create your models here.
class Loan(BaseModel):
    DURATION_CHOICES = (
        ('1','ONE MONTH'),
        ('2','TWO MONTHS'),
        ('3','THREE MONTHS'),
        ('4','FOUR MONTHS'),
    )
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    reason = models.TextField()
    approved_date = models.DateField(blank=True,null=True)
    duration = models.CharField(max_length=20,choices=DURATION_CHOICES)
    guarntee = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE,
    
    )
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    # Higher RQ model fields
    manager_approved = models.BooleanField(default=False)
    manager_rejected = models.BooleanField(default=False)
    coordinator_approved = models.BooleanField(default=False)
    coordinator_rejected = models.BooleanField(default=False)
    executive_approved = models.BooleanField(default=False)
    executive_rejected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.creator.first_name)