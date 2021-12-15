from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class userData(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = ArrayField(models.CharField(max_length=50, null=True, blank= True))
    position = ArrayField(models.CharField(max_length=50, null=True, blank= True))
    injuries = ArrayField(models.CharField(max_length=50, null=True, blank=True))
    fitnessgoal =ArrayField(models.CharField(max_length=50, null=True, blank=True))


    def __str__(self):
        return self.email