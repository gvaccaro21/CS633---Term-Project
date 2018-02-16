from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Measurements(models.Model):
    M_user = models.CharField(max_length=30)
    M_BMI = models.IntegerField(max_length=3)
    M_Height = models.IntegerField(max_length=3)
    M_Weight = models.IntegerField(max_length=3)
