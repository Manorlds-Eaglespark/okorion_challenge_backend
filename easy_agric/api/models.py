from django.db import models

class DistrictDate(models.Model):
    district = models.CharField(max_length=60)
    number = models.IntegerField()
   