import datetime

from django.db import models

from core.models import BaseModel


class RewardPoint(BaseModel):

	STATUS_CHOICE = (('ON_HOLD','ON_HOLD'),('REJECTED','REJECTED'),('APPROVED','APPROVED'))
	YEAR_CHOICES = [(y,y) for y in range(1950, datetime.date.today().year+2)]
	MONTH_CHOICE = [(m,m) for m in range(1,13)]

	user = models.ForeignKey('accounts.User',limit_choices_to={'is_active': True}, on_delete=models.CASCADE)
	year = models.PositiveIntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year,)
	month = models.PositiveIntegerField(choices=MONTH_CHOICE, default=datetime.datetime.now().month,)
	point = models.PositiveIntegerField()
	status = models.CharField(choices=STATUS_CHOICE,max_length=255,default="ON_HOLD")
	description = models.TextField(help_text='add additional information',null=True,blank=True)

	def __str__(self):
		return str(f"{self.user} granted with {self.point} points")
