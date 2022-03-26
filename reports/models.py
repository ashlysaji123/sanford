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
    # higher RQ fields
    supervisor_approved = models.BooleanField(default=False)
    supervisor_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.dar.shop.name
