from django.db import models

# Create your models here.cd
class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length = 100)
    submitter = models.CharField(max_length = 100)
    species = models.CharField(max_length = 50)
    breed = models.CharField(max_length= 50, blank = True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices= SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    vaccination = models.ManyToManyField("Vaccine", blank= True)

class Vaccine(models.Model):
    name= models.CharField(max_length=50)