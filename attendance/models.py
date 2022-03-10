from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _
from location_field.models.plain import PlainLocationField

from core.models import BaseModel


class Attendance(BaseModel):
    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    )
    date = models.DateField(default=now)
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    location = PlainLocationField(based_fields=["city"], zoom=1)
    late_reason = models.TextField(
        verbose_name=_("Reason for being Late"),
        help_text="add additional information for being late",
        null=True,
        blank=True,
    )
    is_leave = models.BooleanField(default=False)
    working_hours = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user}"


class DailyAttendance(models.Model):
    """
    this model is used to record daily attandance informations.
    attandance query will be access from this model.
    """

    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    )
    date = models.DateField()
    working_hours = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    missing_hours = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    is_leave = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"
