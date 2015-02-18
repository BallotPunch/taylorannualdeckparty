from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class InviteCode(models.Model):
	invite_code=models.CharField(max_length=10)
	redeemed=models.BooleanField(default=False)
	def __str__(self):
		return self.invite_code

class Guest(models.Model):
	user=models.ForeignKey(User, unique=True)
	invite_code=models.ForeignKey(InviteCode)
	rsvped=models.BooleanField(default=False)
	rsvp_date=models.DateTimeField(blank=True, null=True)
	attending=models.BooleanField(default=False)
	additionals=models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
	def __str__(self):
		return self.user
