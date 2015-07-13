from django.db import models

# Create your models here.
class Apartment(models.Model):
	name = models.CharField(max_length=120)
	street = models.CharField(max_length=120)
	number = models.IntegerField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	license = models.CharField(max_length=120)

class Owner(models.Model):
	name = models.CharField(max_length=120)
	
