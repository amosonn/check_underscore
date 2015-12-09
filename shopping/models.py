from django.db import models

# Create your models here.

class Car(models.Model):
    pass


class Mall(models.Model):
    parking = models.ManyToManyField(Car)

