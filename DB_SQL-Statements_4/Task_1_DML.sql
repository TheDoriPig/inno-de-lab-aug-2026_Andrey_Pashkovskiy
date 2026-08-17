INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Semen', 'North', 'HR', 57000.00),
('Vlad', 'Black', 'Finance', 62000.00);

SELECT * FROM  Employees;

SELECT 
	firstname,
	lastname 
FROM Employees 
WHERE department = 'IT';

UPDATE Employees
SET salary = 65000.00
WHERE firstname = 'Alice' AND lastname = 'Smith';

DELETE FROM Employees 
WHERE firstname = 'Eve' AND lastname = 'Davis';

SELECT * FROM Employees;