BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Restaurant" (
	"Restaurant_ID"	INT NOT NULL,
	"Name"	VARCHAR(40) NOT NULL,
	"Type"	VARCHAR(40),
	"Dining_Environment"	VARCHAR(40),
	"Number_Total_Employees"	INT,
	"Cuisine"	VARCHAR(40),
	"Max_Capacity"	INT,
	"Meal_Type"	VARCHAR(40),
	"Rating"	INT,
	PRIMARY KEY("Restaurant_ID")
);
CREATE TABLE IF NOT EXISTS "Location" (
	"Location_ID"	INT NOT NULL,
	"Restaurant_ID"	INT NOT NULL,
	"Town"	VARCHAR(40),
	"State"	VARCHAR(40),
	"Address"	VARCHAR(40),
	FOREIGN KEY("Restaurant_ID") REFERENCES "Restaurant"("Restaurant_ID"),
	PRIMARY KEY("Location_ID")
);
CREATE TABLE IF NOT EXISTS "Costs" (
	"Cost_ID"	INT NOT NULL,
	"Rent"	FLOAT,
	"Utilities"	FLOAT,
	"Inventory_Expenses"	FLOAT,
	"Total_Costs"	FLOAT,
	PRIMARY KEY("Cost_ID")
);
CREATE TABLE IF NOT EXISTS "Financials" (
	"Date"	DATE NOT NULL,
	"Restaurant_ID"	INT NOT NULL,
	"Cost_ID"	INT NOT NULL,
	"Revenue_Per_Month"	FLOAT,
	"Costs_Per_Month"	FLOAT,
	"Net_Profit_Per_Month"	FLOAT,
	FOREIGN KEY("Restaurant_ID") REFERENCES "Restaurant"("Restaurant_ID"),
	FOREIGN KEY("Cost_ID") REFERENCES "Costs"("Cost_ID"),
	PRIMARY KEY("Date")
);
CREATE TABLE IF NOT EXISTS "Employee" (
	"Employee_ID"	INT NOT NULL,
	"Restaurant_ID"	INT NOT NULL,
	"Name"	VARCHAR(40),
	"Job_Type"	VARCHAR(40),
	"Hourly_Salary"	FLOAT,
	"Weekly_Hours"	FLOAT,
	"Weekly_Salary"	FLOAT,
	"Employee_Satisfaction"	INT,
	FOREIGN KEY("Restaurant_ID") REFERENCES "Restaurant"("Restaurant_ID"),
	PRIMARY KEY("Employee_ID")
);
CREATE TABLE IF NOT EXISTS "Rewards_Program" (
	"Customer_ID"	INT NOT NULL,
	"Restaurant_ID"	INT NOT NULL,
	"Program_Name"	VARCHAR(40) NOT NULL,
	"Total_Points"	INT,
	"Cumulative_Rewards_Used"	INT,
	"Customer_Name"	VARCHAR(40) NOT NULL,
	FOREIGN KEY("Restaurant_ID") REFERENCES "Restaurant"("Restaurant_ID"),
	PRIMARY KEY("Customer_ID")
);
COMMIT;
