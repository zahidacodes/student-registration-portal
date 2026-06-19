from django.db import models

# Create your models here.
class myclass(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    branch = models.CharField(max_length=5)
    ph_number = models.IntegerField()
