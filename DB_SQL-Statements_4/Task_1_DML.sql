--Insert new employees
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Semen', 'North', 'HR', 57000.00),
('Vlad', 'Black', 'Finance', 62000.00);

--Select all columns from employees table
SELECT * FROM  Employees;

--Select full name of employees working in the IT department
SELECT 
	firstname,
	lastname 
FROM Employees 
WHERE department = 'IT';

--Update salary for Alice Smith 
UPDATE Employees
SET salary = 65000.00
WHERE firstname = 'Alice' AND lastname = 'Smith';

--Delete Eve Davis
DELETE FROM Employees 
WHERE firstname = 'Eve' AND lastname = 'Davis';

--Checking the result
SELECT * FROM Employees;