from django.db import models

from core.models import BaseModel


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
    is_completed = models.BooleanField(default=False)
    time_taken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.executive.name} - {self.shop.name}"


class DARNotes(BaseModel):
    dar = models.ForeignKey(
        DARTask, limit_choices_to={"is_deleted": False}, 
        on_delete=models.CASCADE, 
        blank=True, null=True
    )
    title = models.CharField(max_length=221)
    note = models.CharField(max_length=221, blank=True, null=True)

    def __str__(self):
        return self.dar.executive.name


class DARReschedule(BaseModel):
    dar = models.ForeignKey(
        DARTask, limit_choices_to={"is_deleted": False}, on_delete=models.CASCADE
    )
    reschedule_date = models.DateField("Reschedule date")
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.dar.shop.name
