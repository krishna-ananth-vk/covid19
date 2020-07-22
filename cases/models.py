from django.db import models

# Create your models here.



class District(models.Model):

    name = models.CharField(max_length=20)

    id = models.IntegerField(primary_key=True)

    hosptals = models.IntegerField()

    Confirmed = models.IntegerField()

    Recovered = models.IntegerField()

    Death = models.IntegerField()

    Active = models.IntegerField()
    

class Case(models.Model):

    id = models.IntegerField(primary_key=True)

    dis = models.ForeignKey("District",on_delete=models.SET_NULL,null =True)

    gender = models.CharField(max_length=1)
    
    age = models.IntegerField()

class DateReport(models.Model):

    date = models.DateField(primary_key=True)

    confirmed = models.IntegerField()
    Active = models.IntegerField()
    Death = models.IntegerField()
    Recovered = models.IntegerField()
    

class TestReport(models.Model):
    
    date = models.DateField(primary_key=True)
    total_sent = models.IntegerField()
    sent = models.IntegerField()
    total_positive = models.IntegerField()
    new_positive = models.IntegerField()


