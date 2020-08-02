from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=10)
    name_wo_diacritics = models.CharField(max_length=128)
    country = models.CharField(max_length=2, null=True, blank=True)
    location = models.CharField(max_length=3, null=True, blank=True)
    subdivision = models.CharField(max_length=3)
    status = models.CharField(max_length=2)
    function = models.CharField(max_length=8)
    date = models.CharField(max_length=4, null=True, blank=True)
    IATA = models.CharField(max_length=3, null=True, blank=True)
