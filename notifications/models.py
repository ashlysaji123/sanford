from django.db import models
from django.utils.timesince import timesince

from core.models import BaseModel


class Notification(BaseModel):
    NOTIFICATION_TYPE_CHOICES = (
        ("PRODUCT", "PRODUCT"),
        ("ALERT", "ALERT"),
        ("VOTING", "VOTING"),
        ("NOTIFICATION", "NOTIFICATION"),
    )

    title = models.CharField(max_length=128)
    type = models.CharField(
        max_length=128, choices=NOTIFICATION_TYPE_CHOICES, default="NOTIFICATION"
    )
    description = models.TextField()

    def __str__(self):
        return str(self.title)

    def created_at(self):
        return timesince(self.created)
