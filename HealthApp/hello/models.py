from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    M_BMI = models.IntegerField()
    M_Height = models.IntegerField()
    M_Weight = models.IntegerField()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=50, default="")
    website = models.URLField(default="")
    phone = models.IntegerField(default=0)
