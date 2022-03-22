from django.db import models

from core.models import BaseModel
# Create your models here.
class Loan(BaseModel):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    max_amount = models.DecimalField(max_digits=10,decimal_places=2)
    reason = models.TextField()
    date = models.DateField()
    duration = models.CharField(max_length=200)
    user = user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    ) 
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.employe_id)