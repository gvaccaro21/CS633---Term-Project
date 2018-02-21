from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
import logging

from .models import Greeting, Measurements
# Import messages
from django.contrib import messages

logger = logging.getLogger(__name__)

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
    else:
        form = UserCreationForm()
        args = {'form': form}
        # Return messages
        messages.warning(request, "User already exists or password doesn't match criteria")
        
        return render(request, 'register.html', args)

def welcome(request):
    # return the Main site page
    #usrmeasurements = Measurements.objects.get(user_id=int(request.user.id))
    usrmeasurements = Measurements.objects.filter(user_id=int(request.user.id)).values()
    #logger.warning(">>>> INFO:"+str(usrmeasurements.M_BMI))
    args = {"usrmeasurements": usrmeasurements}
    return render(request, 'welcome.html', args)

def index(request):
    # return the Main site page
    return render(request, 'index.html')

def logout(request):
    # Log the user out of the application
    django_logout(request)
    return render(request, 'index.html')

def measure(request):
    # return the Measurements Page
    usrmeasurements = Measurements.objects.all()
    args = {"usrmeasurements": usrmeasurements}
    return render(request, 'measure.html', args)

def savemeasurements(request):
    from hello.forms import MeasurementsForm
    #logger.warning(">>>> INFO: The current user id is: "+str(request.user.id))
    if Measurements.objects.filter(user_id=int(request.user.id)).exists():       
        MyMeasurements = Measurements.objects.get(user_id=int(request.user.id))
        myform = MeasurementsForm(request.POST, instance=MyMeasurements)
    else: 
        myform = MeasurementsForm(request.POST)
    if myform.is_valid():
        # logger.info(">>>> INFO:"+text)         
        MyMeasurements = myform.save(commit=False)
        MyMeasurements.user = request.user
        MyMeasurements.save()
    return redirect("welcome")
    
    # try: 
    #     username = request.user.userprofile
    # except UserProfile.DoesNotExist:
    #     username = UserProfile(user=request.user)
    # if request.method =="POST":        
    #     intBMI = request.POST.get("inputBMI", "")
    #     intHeight = request.POST.get("inputHeight", "")
    #     intWeight = request.POST.get("inputWeight", "")
    #     objMeasurments = Measurements(user = username, M_BMI = intBMI, M_Height = intHeight, M_Weight = intWeight)
    #     objMeasurments.save()   

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

