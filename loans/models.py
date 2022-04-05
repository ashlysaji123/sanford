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
    guarantee = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE,
    )
    paid_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    is_returned_completely = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    # Higher RQ model fields
    global_manager_approved = models.BooleanField(default=False)
    global_manager_rejected = models.BooleanField(default=False)
    manager_approved = models.BooleanField(default=False)
    manager_rejected = models.BooleanField(default=False)
    coordinator_approved = models.BooleanField(default=False)
    coordinator_rejected = models.BooleanField(default=False)
    supervisor_approved = models.BooleanField(default=False)
    supervisor_rejected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.creator.first_name} - {self.amount}"


class LoanLog(BaseModel):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    date = models.DateField()
    carrier = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE,
    )
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    def get_absolute_url(self):
        return reverse("loans:view_loan", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("loans:update_loan", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("loans:delete_loan", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.loan.creator.first_name} - {self.loan.amount}"