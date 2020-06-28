from django.db import models
from django.utils import timezone

# Create your models here.


class Genere(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
