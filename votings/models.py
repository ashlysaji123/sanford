from django.db import models
import uuid

# Create your models here.
class VotingItem(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    voting_startdate = models.DateField()
    voting_enddate = models.DateField()

    def __str__(self):
        return str(self.product.name)

class Voting(models.Model):
    CHOICES = (
        ('bad','BAD'),
        ('good','GOOD'),
        ('perfect','PERFECT'),
    )
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )
    voting_item = models.ForeignKey(VotingItem,on_delete=models.CASCADE,null=True)
    voting = models.CharField(max_length=250,choices=CHOICES)
    user = models.ForeignKey("accounts.User", limit_choices_to={"is_active": True},on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.first_name)


    
    