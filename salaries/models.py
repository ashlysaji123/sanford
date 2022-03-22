from django.db import models
from core.models import BaseModel

# Create your models here.

class SalaryAdavance(BaseModel):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    ) 
    date = models.DateField()
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    max_amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.user.username)