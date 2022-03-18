from django.db import models


# Create your models here.

class Restaurant(models.Model):
    Restaurant_Id = models.IntegerField(primary_key=True, null=False)
    Name = models.CharField(max_length=40, null=False)
    Type = models.CharField(max_length=40)
    Dining_Environment = models.CharField(max_length=40)
    Number_Total_Employees = models.IntegerField()
    Cuisine = models.CharField(max_length=40)
    Max_Capacity = models.IntegerField()
    Meal_Type = models.CharField(max_length=40)

    choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    Rating = models.IntegerField(choices=choices)

    def __str__(self):
        return 'Restaurant_Id : {0} Name : {1} Type : {2}'.format(self.Restaurant_Id, self.Name, self.Type)

class Employee(models.Model):
    Employee_Id = models.IntegerField(primary_key=True, null=False)
    Restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)
    Name = models.CharField(max_length=40, null=False)
    Job_Type = models.CharField(max_length=40)
    Hourly_Salary = models.FloatField()
    Weekly_Hours = models.FloatField()
    Weekly_Salary = models.F(Hourly_Salary) * models.F(Weekly_Hours)

    choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    Satisfaction = models.IntegerField(choices=choices)

    def __str__(self):
        return 'Employee_ID : {0} Name : {1} Job_Type : {2}'.format(self.Employee_Id, self.Name, self.Job_Type)

class Location(models.Model):
    Location_Id = models.IntegerField(primary_key=True, null=False)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Town = models.CharField(max_length=40)
    State = models.CharField(max_length=40)
    Address = models.CharField(max_length=40)


class Cost(models.Model):
    Cost_Id = models.IntegerField(primary_key=True,null=False)
    Rent = models.FloatField()
    Utilities = models.FloatField()
    Inventory_Expenses = models.FloatField()
    Total_Costs = models.FloatField()


class Financial(models.Model):
    Financial_Id = models.IntegerField(primary_key=True)
    Date = models.DateField(null=False)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Cost = models.ForeignKey(Cost, on_delete=models.CASCADE)
    Revenue_Per_Month = models.FloatField()
    Costs_Per_Month = models.FloatField()
    Net_Profit_Per_Month = models.FloatField()


class Rewards_Program(models.Model):
    Customer_Id = models.IntegerField(primary_key=True,null=False)
    Customer_Name = models.CharField(null=False, max_length=40)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Program_Name = models.CharField(max_length=40)
    Total_Points = models.FloatField()
    Cumulative_Points_Used = models.IntegerField(default=0)
