from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def display_Restaurant(request):
    items = Restaurant.objects.all()

    context = {
        "items": items,
        "header": "Restaurant"
    }

    return render(request, 'index.html', context)

def display_Employee(request):
    items = Employee.objects.all()

    context = {
        "items": items,
        "header" : "Employee"
    }

    return render(request, 'index.html', context)

def display_Location(request):
    items = Location.objects.all()

    context = {
        "items": items,
        "header" : "Location"
    }

    return render(request, 'index.html', context)

def display_Financial(request):
    items = Financial.objects.all()

    context = {
        "items": items,
        "header" : "Financial"
    }

    return render(request, 'index.html', context)

def display_Cost(request):
    items = Cost.objects.all()

    context = {
        "items": items,
        "header": "Cost"
    }

    return render(request, 'index.html', context)

def display_Rewards(request):
    items = Rewards_Program.objects.all()

    context = {
        "items": items,
        "header": "Rewards"
    }

    return render(request, 'index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_Restaurant(request):
    return add_item(request, RestaurantForm)

def add_Employee(request):
    return add_item(request, EmployeeForm)

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
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_Restaurant(request,pk):
    return edit_item(request, pk, Restaurant, RestaurantForm)

def edit_Employee(request,pk):
    return edit_item(request, pk, Employee, EmployeeForm)

def edit_Location(request,pk):
    return edit_item(request, pk, Location, LocationForm)

def edit_Financial(request,pk):
    return edit_item(request, pk, Financial, FinancialForm)

def edit_Cost(request,pk):
    return edit_item(request, pk, Cost, CostForm)

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