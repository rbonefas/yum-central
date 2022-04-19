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
    con = sqlite3.connect(BASE_DIR/ 'db.sqlite3')
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

del_num_employees(1)