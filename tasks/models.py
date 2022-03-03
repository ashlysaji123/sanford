from django.db import models

from core.models import BaseModel
from accounts.models import User
# Create your models here.


class Tasks(BaseModel):
    task = models.TextField("Enter task")
    user = models.ForeignKey('accounts.User',limit_choices_to={'is_active': True}, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.task