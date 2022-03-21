from django.db import models

from core.models import BaseModel

# Create your models here.
class EmployeeDocuments(BaseModel):
    user = models.ForeignKey(
        "accounts.User", limit_choices_to={"is_active": True}, on_delete=models.CASCADE
    )
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.user.employe_id


class EmployeeDocumentsItems(BaseModel):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to="document")

    def __str__(self):
        return self.title