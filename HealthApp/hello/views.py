from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Measurements

# Create your views here.
def index(request):
    # return the Main site page
    return render(request, 'index.html')

def measure(request):
    # return the Measurements Page
    return render(request, 'measure.html')

def savemeasurements(request):
    if request.method =="POST":
        user = ""
        intBMI = request.POST.get("inputBMI", "")
        intHeight = request.POST.get("inputHeight", "")
        intWeight = request.POST.get("inputWeight", "")
        objMeasurments = Measurements(M_user = user, M_BMI = intBMI, M_Height = intHeight, M_Weight = intWeight)
        objMeasurments.save()   

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

