from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()

    def __iter__(self):
        return iter(self.name)

    def __unicode__(self):
        return self.name

class Apartment(models.Model):
    id_2 = models.IntegerField(default= None)
    neighborhood = models.CharField(max_length=100)
    name = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    created = models.DateTimeField()
    cats = models.ManyToManyField(Category)
    address = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()



    def __unicode__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=120)

    objects = models.Manager()

    def __unicode__ (self):
        return self.name

