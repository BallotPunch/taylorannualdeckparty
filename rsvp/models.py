from django.db import models

# Create your models here.
class Guest(models.Model):
	first_name=models.CharField(max_length=75)
	last_name=models.CharField(max_length=75)
	invite_code=models.ForeignKey(Code)
	rsvped=models.BooleanField()
	additionals=IntegerField(default=0, validators=[MaxValueValidator(5),MinValueValidator(0)])a

class InviteCode(models.Model):
	invite_code=models.CharField(max_length=10)
	redeemed=models.BooleanField()
