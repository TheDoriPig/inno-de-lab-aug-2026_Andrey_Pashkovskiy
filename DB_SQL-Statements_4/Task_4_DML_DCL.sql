UPDATE Employees 
SET salary = salary * 1.10
WHERE department = 'HR';

UPDATE Employees
SET department = 'Senior IT'
WHERE employeeid = (
	SELECT employeeid 
	FROM Employees
	WHERE salary > 70000.00
	LIMIT 1
);

DELETE FROM Employees e
WHERE NOT EXISTS (
	SELECT 1
	FROM EmployeeProjects ep
	WHERE ep.employeeid = e.employeeid 
);

BEGIN;
	
	
	INSERT INTO Projects (projectid, projectname, budget, startdate, enddate) VALUES
	(4, 'Software Development', 100000, '2023-07-20', '2023-11-12');
	
	
	INSERT INTO EmployeeProjects (employeeid, projectid, hoursworked) VALUES 
	(3, 4, 110),
	(4, 4, 120);
	
COMMIT;
ROLLBACK;