from django import forms

class MeasurementsForm(forms.ModelForm):
    M_BMI = forms.IntegerField()
    M_Height = forms.IntegerField()
    M_Weight = forms.IntegerField()

    class Meta:
        from .models import Measurements        
        model = Measurements
        fields = ("M_BMI", "M_Height", "M_Weight")
