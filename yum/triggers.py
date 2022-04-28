import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def add_num_employees(ri):
    con = sqlite3.connect(BASE_DIR / 'db.sqlite3')
    cur = con.cursor()
    cur.execute('''
    UPDATE yum_restaurant
    SET "Number_Total_Employees" = "Number_Total_Employees" + 1 
    WHERE Restaurant_Id = {};
    '''.format(ri))
    con.commit()


def del_num_employees(e_id):
    con = sqlite3.connect(BASE_DIR / 'db.sqlite3')
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
    con = sqlite3.connect(BASE_DIR / 'db.sqlite3')
    cursor = con.cursor()

    cursor.execute(''' 
                UPDATE yum_cost
                SET Total_Costs = Total_Salaries + Rent + Utilities + Inventory_Expenses
                WHERE Cost_id = {};'''.format(id))
    con.commit()

    cursor.execute(''' 
    UPDATE yum_financial
    SET Costs_Per_Month = ( SELECT Total_Costs FROM yum_cost WHERE Cost_id = {})
    WHERE Cost_id = {};'''.format(id, id))
    con.commit()



def update_weekly_salary(ri, ei):
    con = sqlite3.connect(BASE_DIR / 'db.sqlite3')
    cur = con.cursor()
    cur.execute(''' 
    UPDATE yum_cost 
    SET total_salaries = ( 
        SELECT SUM(e2.hourly_salary * e2.weekly_hours)  
        FROM yum_employee e2 
        WHERE e2.restaurant_id = {} 
    ) 
    WHERE cost_id = ( 
        SELECT c.cost_id  
        FROM yum_cost c 
        JOIN yum_financial f on c.cost_id = f.cost_id 
        JOIN yum_employee e on e.restaurant_id = f.restaurant_id 
        WHERE e.employee_id = {} 
    ) 
    '''.format(ri, ei))
    con.commit()


def totalCostExpenses(cost_id):
    con = sqlite3.connect(BASE_DIR / 'db.sqlite3')
    cursor = con.cursor()
    cursor.execute('''
            UPDATE yum_cost
            SET Total_Costs = Total_Salaries + Rent + Utilities + Inventory_Expenses 
            WHERE Cost_Id = {}; 
            '''.format(cost_id))

    con.commit()


def calculateNetFinancial(id):
    con = sqlite3.connect(BASE_DIR / 'db.sqlite3')
    cursor = con.cursor()
    cursor.execute('''
                UPDATE yum_financial
                SET Net_Profit_Per_Month = Revenue_Per_Month - Costs_Per_Month
                WHERE Financial_id = {};
                '''.format(id))

    con.commit()
