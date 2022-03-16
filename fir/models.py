from django.db import models

# Create your models here.
class Helpline(models.Model):
    name = models.CharField(max_length=20, default='Emergency')
    number = models.BigIntegerField(blank=True)

class Vote(models.Model):

    vote = models.PositiveIntegerField(primary_key=True, blank=True, default=0)

class Report(models.Model):

    types = (('Dacoity', 'Dacoity'), ('Robbery', 'Robbery'), ('Rape', 'Rape'))

    name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.BigIntegerField(blank=True)
    address = models.TextField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    crime_type = models.CharField(max_length=50, choices=types)
    desc = models.TextField(max_length=255, blank=True, null=True)
    proof = models.FileField(upload_to='', blank=True)
    votes = models.ForeignKey(Vote, null=True, on_delete=models.CASCADE)
    option = models.BooleanField()