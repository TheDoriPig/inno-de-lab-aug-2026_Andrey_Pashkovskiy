--Increase the salaries of all employees by 10% 
UPDATE Employees 
SET salary = salary * 1.10
WHERE department = 'HR';

--Transferring employees who salary over 70,000 to a new department
UPDATE Employees
SET department = 'Senior IT'
WHERE salary > 70000.00;

--Delete employees who are not assigned to projects
DELETE FROM Employees e
WHERE NOT EXISTS (
	SELECT 1
	FROM EmployeeProjects ep
	WHERE ep.employeeid = e.employeeid 
);

--Сreat a new project and immediately assigning employees to it
BEGIN;
	
	INSERT INTO Projects (projectid, projectname, budget, startdate, enddate) VALUES
	(4, 'Software Development', 100000, '2023-07-20', '2023-11-12');
	
	INSERT INTO EmployeeProjects (employeeid, projectid, hoursworked) VALUES 
	(3, 4, 110),
	(4, 4, 120);
	
COMMIT;
