from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModel


class LeaveRequest(BaseModel):
    LEAVE_TYPE = (
        ("sick", "Sick Leave"),
        ("casual", "Casual Leave"),
        ("emergency", "Emergency Leave"),
        ("study", "Study Leave"),
        ("annual", "Annual Leave"),
        ("maternity", "Maternity Leave"),
        ("paternity", "Paternity Leave"),
        ("bereavement", "Bereavement Leave"),
        ("quarantine", "Self Quarantine"),
        ("compensatory", "Compensatory Leave"),
        ("sabbatical", "Sabbatical Leave"),
    )
    user = models.ForeignKey(
        "accounts.User",
        limit_choices_to={"is_active": True},
        on_delete=models.CASCADE,
        default=1,
    )
    startdate = models.DateField(
        verbose_name=_("Start Date"), help_text="leave start date is on .."
    )
    enddate = models.DateField(
        verbose_name=_("End Date"), help_text="coming back on ..."
    )
    leavetype = models.CharField(choices=LEAVE_TYPE, max_length=25, default="sick")
    reason = models.TextField(
        verbose_name=_("Reason for Leave"),
        help_text="add additional information for leave",
        null=True,
        blank=True,
    )
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    total_available_leave = models.PositiveIntegerField(default=12)
    leave_duration = models.PositiveIntegerField(default=0)
    # Higher RQ model fields
    manager_approved = models.BooleanField(default=False)
    manager_rejected = models.BooleanField(default=False)
    coordinator_approved = models.BooleanField(default=False)
    coordinator_rejected = models.BooleanField(default=False)
    supervisor_approved = models.BooleanField(default=False)
    supervisor_rejected = models.BooleanField(default=False)
    executive_approved = models.BooleanField(default=False)
    executive_rejected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.leavetype} - {self.user}"

    @property
    def leave_days(self):
        startdate = self.startdate
        enddate = self.enddate
        if startdate > enddate:
            return
        dates = enddate - startdate
        return (dates.days + 1)
