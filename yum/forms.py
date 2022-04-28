from django import forms
from .models import *
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        exclude = ["Number_Total_Employees"]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class FinancialForm(forms.ModelForm):
    class Meta:
        model = Financial
        fields = '__all__'


class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'
        exclude = ["Total_Salaries","Total_Costs"]

class RewardsForm(forms.ModelForm):
    class Meta:
        model = Rewards_Program
        fields = '__all__'

