from django.db import models
# Create your models here.

class Electric(models.Model):
    ServiceAddress = models.CharField(max_length=120)
    Month = models.CharField(max_length=20)
    Year = models.CharField(max_length=4)
    KWH_Consumption = models.IntegerField()
    Charge = models.IntegerField(default=0)

class Water(models.Model):
    ServiceAddress = models.CharField(max_length=120)
    Month = models.CharField(max_length=20)
    Year = models.CharField(max_length=4)
    Water_Consumption = models.IntegerField()
    Charge = models.IntegerField(default=0)