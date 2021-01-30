from django.db import models

# Create your models here.cd
class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField("Vaccine", blank= True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)


class Humans(models.Model):
    sex = [("M", "Male"),("F", "Female"),("A","Agender"),("B","Bigender"),("P","Polygender"),("G","Genderfliud"),("GQ","Genderqueer"),("N","Non-binary")]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=True)
    gender= models.CharField(max_length=2,choices=sex)
    address = models.CharField(max_length=100)