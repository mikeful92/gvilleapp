from django.db import models
# Create your models here.

class Consumption(models.Model):
    ServiceAddress = models.CharField(max_length=120)
    Month = models.CharField(max_length=20)
    Year = models.CharField(max_length=4)
    KWH_Consumption = models.IntegerField(null=True)