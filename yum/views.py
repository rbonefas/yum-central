from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from .triggers import *
from .filters import *

# Create your views here.


def index(request):
    return render(request, 'index.html')

def display_Restaurant(request):
    items = Restaurant.objects.all()

    filter = RestaurantFilter(request.GET,queryset=items)

    items = filter.qs
    context = {
        "items": items,
        "header": "Restaurant",
        "rest_filter": filter
    }


    return render(request, 'index.html', context)

def display_Employee(request):
    items = Employee.objects.all()
    filter = EmployeeFilter(request.GET, queryset=items)
    items = filter.qs
    context = {
        "items": items,
        "header" : "Employee",
        "emp_filter": filter
    }

    return render(request, 'index.html', context)

def display_Location(request):
    items = Location.objects.all()
    filter = LocationFilter(request.GET, queryset=items)
    items = filter.qs
    context = {
        "items": items,
        "header" : "Location",
        "loc_filter": filter
    }

    return render(request, 'index.html', context)

def display_Financial(request):
    items = Financial.objects.all()
    filter = FinancialFilter(request.GET, queryset=items)
    items = filter.qs
    context = {
        "items": items,
        "header" : "Financial",
        "fin_filter":filter
    }

    return render(request, 'index.html', context)

def display_Cost(request):
    items = Cost.objects.all()
    filter = CostFilter(request.GET, queryset=items)
    items = filter.qs
    context = {
        "items": items,
        "header": "Cost",
        "cost_filter": filter
    }

    return render(request, 'index.html', context)

def display_Rewards(request):
    items = Rewards_Program.objects.all()
    filter = RewardsFilter(request.GET, queryset=items)
    items = filter.qs
    context = {
        "items": items,
        "header": "Rewards",
        "rew_filter": filter
    }

    return render(request, 'index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_Restaurant(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    else:
        form = RestaurantForm()
        return render(request, 'add_new.html', {'form': form})

def add_Employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            add_num_employees(form.cleaned_data.get("Restaurant"))
            return redirect('index')

    else:
        form = EmployeeForm()
        return render(request, 'add_new.html', {'form': form})

def add_Location(request):
    return add_item(request, LocationForm)

def add_Financial(request):
    return add_item(request, FinancialForm)

def add_Cost(request):
    return add_item(request, CostForm)

def add_Rewards(request):
    return add_item(request, RewardsForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_Restaurant(request,pk):
    return edit_item(request, pk, Restaurant, RestaurantForm)

def edit_Employee(request,pk):
    item = get_object_or_404(Employee, pk=pk)
    cls = EmployeeForm
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save(commit=True)
            update_weekly_salary(form.cleaned_data.get("Restaurant"))
            totalCostExpenses(pk)
            updateCosts(pk)
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_Location(request,pk):
    return edit_item(request, pk, Location, LocationForm)

def edit_Financial(request,pk):
    return edit_item(request, pk, Financial, FinancialForm)

def edit_Cost(request,pk):
    item = get_object_or_404(Cost, pk=pk)
    cls = CostForm
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save(commit=True)
            updateCosts(pk)
            totalCostExpenses(pk)
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_Rewards(request,pk):
    return edit_item(request, pk, Rewards_Program, RewardsForm)

def delete_Restaurant(request, pk):

    template = 'index.html'
    Restaurant.objects.filter(pk=pk).delete()

    items = Restaurant.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Employee(request, pk):

    template = 'index.html'

    del_num_employees(pk)
    Employee.objects.filter(pk=pk).delete()


    items = Employee.objects.all()




    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Location(request, pk):

    template = 'index.html'
    Location.objects.filter(pk=pk).delete()

    items = Location.pk

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Financial(request, pk):

    template = 'index.html'
    Financial.objects.filter(pk=pk).delete()

    items = Financial.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Cost(request, pk):

    template = 'index.html'
    Cost.objects.filter(pk=pk).delete()

    items = Cost.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Rewards(request, pk):

    template = 'index.html'
    Rewards_Program.objects.filter(pk=pk).delete()

    items = Rewards_Program.objects.all()

    context = {
        'items': items,
    }
    return render(request, template, context)


def display_Restaurant_Report(request):
    items = Restaurant.objects.all()
    context = {
        "items": items,
        "header" : "Restaurant_Report"
    }

    return render(request, 'index.html', context)