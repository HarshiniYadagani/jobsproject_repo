from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=500)
    role=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    location=models.CharField(max_length=65)
    email=models.EmailField()
    contactnumber=models.BigIntegerField()

class Banglorejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=500)
    role=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    location=models.CharField(max_length=64)
    email=models.EmailField()
    contactnumber=models.BigIntegerField()

class Punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=500)
    role=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    location=models.CharField(max_length=65)
    email=models.EmailField()
    contactnumber=models.BigIntegerField()
