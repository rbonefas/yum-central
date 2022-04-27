import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def add_num_employees(ri):
    con = sqlite3.connect(BASE_DIR/ 'db.sqlite3')
    cur = con.cursor()
    cur.execute('''
    UPDATE yum_restaurant
    SET "Number_Total_Employees" = "Number_Total_Employees" + 1 
    WHERE Restaurant_Id = {};
    '''.format(ri))
    con.commit()


def del_num_employees(e_id):
    con = sqlite3.connect(BASE_DIR/'db.sqlite3')
    cur = con.cursor()

    cur.execute('''
    SELECT Restaurant_id FROM yum_employee
    WHERE (Employee_Id = {});
    '''.format(e_id))

    ri = cur.fetchall()[0][0]

    cur.execute('''
    UPDATE yum_restaurant
    SET "Number_Total_Employees" = "Number_Total_Employees" - 1 
    WHERE (Restaurant_Id = {});
    '''.format(ri))
    con.commit()


def updateCosts(id):
    con = sqlite3.connect(BASE_DIR/'db.sqlite3')
    cursor = con.cursor()
    cursor.execute(''' 
    UPDATE yum_financial
    SET Costs_Per_Month = ( SELECT Total_Costs FROM yum_cost WHERE Cost_id = {})
    WHERE Cost_id = {};'''.format(id,id))
    con.commit()


def update_weekly_salary(ri):

    con = sqlite3.connect(BASE_DIR /'db.sqlite')

    cur = con.cursor()

    cur.execute('''UPDATE yum_costs   
    
    SET Total_Salaries = (SELECT SUM(Weekly_Salary) FROM yum_employee 
    
    WHERE employee_id = {} ) 
    
    JOIN yum_financial f ON yum_costs.cost_id = f.cost_id  
    JOIN yum_restaurant r ON f.restaurant_id = r.restaurant_id 
    
    WHERE yum_employee.employee_id = {}'''.format(ri, ri))

    con.commit()



def totalCostExpenses(cost_id):
    con = sqlite3.connect(BASE_DIR/'db.sqlite3')
    cursor = con.cursor()
    cursor.execute('''
            UPDATE yum_cost
            SET Total_Costs = Total_Salaries + Rent + Utilities + Inventory_Expenses 
            WHERE Cost_Id = {}; 
            '''.format(cost_id))

    con.commit()