import django_filters

from .models import *

class RestaurantFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = ["Cuisine","Dining_Environment"]

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ["Restaurant","Job_Type"]

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = ["State"]

class FinancialFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="Date", lookup_expr='gte',label='Start Date')
    end_date = django_filters.DateFilter(field_name="Date", lookup_expr='lte',label="End Date")
    class Meta:
        model = Financial
        fields = ["Restaurant"]

class CostFilter(django_filters.FilterSet):
    class Meta:
        model = Cost
        fields = '__all__'

class RewardsFilter(django_filters.FilterSet):
    class Meta:
        model = Rewards_Program
        fields = ["Restaurant"]