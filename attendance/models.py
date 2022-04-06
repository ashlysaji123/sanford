from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _
from location_field.models.plain import PlainLocationField
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import BaseModel
from accounts.models import User
# from django.conf import settings

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




""" signal functions for creating users """
# @receiver(post_save, sender=Attendance)
# def create_daily_attendance(sender, instance, created, **kwargs):
#     if not DailyAttendance.objects.filter(user=instance.user,date=instance.date).exists():
#         daily_attendance  = DailyAttendance.objects.create(
#             user=instance.user,
#             date=instance.date
#         )
#         instance.attendance = daily_attendance
#         instance.save()
#     else:
#         daily_attendance = DailyAttendance.objects.get(pk=instance.attendance.pk)
#         daily_attendance.working_hours = instance.working_hours
#         daily_attendance.missing_hours = settings.SANFORDCORP_WORKING_HOURS - daily_attendance.working_hours
#         daily_attendance.save()

""" end signals """

