from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _
from location_field.models.plain import PlainLocationField
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import BaseModel
from accounts.models import User
from django.conf import settings

class DailyAttendance(models.Model):
    """
    this model is used to record daily attandance informations.
    attandance query will be access from this model.
    """
    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    )
    date = models.DateField()
    working_hours = models.TimeField(blank=True, null=True)
    missing_hours = models.TimeField(blank=True, null=True)
    late_reason = models.TextField(null=True,blank=True)
    is_leave = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)
    first_check_in = models.TimeField(blank=True, null=True)
    last_check_out = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


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
    is_late = models.BooleanField(default=False)
    is_leave = models.BooleanField(default=False)
    working_hours = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"




""" signal functions for creating users """
@receiver(post_save, sender=Attendance)
def create_daily_attendance(sender, instance, created, **kwargs):
    if not DailyAttendance.objects.filter(user=instance.user,date=instance.date).exists():
        daily_attendance  = DailyAttendance.objects.create(
            user=instance.user,
            date=instance.date,
            first_check_in= instance.check_in_time,
            late_reason=instance.late_reason,
            is_late=instance.is_late
        )
    else:
        daily_attendance = DailyAttendance.objects.get(user=instance.user,date=instance.date)
        daily_attendance.last_check_out = instance.check_out_time
        daily_attendance.working_hours += instance.working_hours
        daily_attendance.missing_hours = settings.SANFORDCORP_WORKING_HOURS - daily_attendance.working_hours
        daily_attendance.save()

""" end signals """

