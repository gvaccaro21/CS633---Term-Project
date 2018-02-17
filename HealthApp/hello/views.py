from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
import logging

from .models import Greeting, Measurements

# Create your views here.
def register(request):
    # return the register page
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome.html')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'register.html', args)

def index(request):
    # return the Main site page
    return render(request, 'index.html')

def measure(request):
    # return the Measurements Page
    usrmeasurements = Measurements.objects.all()
    args = {"usrmeasurements": usrmeasurements}
    return render(request, 'measure.html', args)

def savemeasurements(request):
    if request.method =="POST":
        user = ""
        intBMI = request.POST.get("inputBMI", "")
        intHeight = request.POST.get("inputHeight", "")
        intWeight = request.POST.get("inputWeight", "")
        objMeasurments = Measurements(M_user = user, M_BMI = intBMI, M_Height = intHeight, M_Weight = intWeight)
        objMeasurments.save()   
        return redirect("index")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

