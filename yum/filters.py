import django_filters

from .models import *

class RestaurantFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = '__all__'

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = '__all__'

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = '__all__'

class FinancialFilter(django_filters.FilterSet):
    class Meta:
        model = Financial
        fields = '__all__'

class CostFilter(django_filters.FilterSet):
    class Meta:
        model = Cost
        fields = '__all__'

class RewardsFilter(django_filters.FilterSet):
    class Meta:
        model = Rewards_Program
        fields = '__all__'