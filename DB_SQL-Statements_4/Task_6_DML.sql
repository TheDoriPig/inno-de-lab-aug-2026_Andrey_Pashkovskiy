--Select project names where Bob Johnson worked more than 150 hours
SELECT 
	p.projectname 
FROM projects p 
JOIN employeeprojects ep ON p.projectid = ep.projectid
JOIN employees e ON ep.employeeid = e.employeeid 
WHERE e.firstname = 'Bob' AND e.lastname = 'Johnson' AND ep.hoursworked > 150;

--------------------------------------------------------------------------------
--Increase the budget by 10% for projects that have IT department employees assigned
UPDATE projects p 
SET Budget = Budget * 1.10
WHERE EXISTS (
	SELECT 1
	FROM employeeprojects ep
	JOIN employees e ON ep.employeeid = e.employeeid 
	WHERE ep.projectid = p.projectid AND e.department = 'IT'
);

--Retrieve project IDs, names, and budgets to verify the budget update
SELECT p.projectid, p.projectname, p.budget 
FROM projects p;

--------------------------------------------------------------------------------
--Set the project enddate a year later startdate if enddate is NULL
UPDATE projects
SET enddate = startdate + INTERVAL '1 year'
WHERE enddate IS NULL 

--Checking update
SELECT p.projectid, p.projectname, p.startdate, p.enddate 
FROM projects p 

--------------------------------------------------------------------------------
--Executed the transaction to add a new employee and assign them to a project
BEGIN;
	WITH new_employee AS (
	INSERT INTO employees (firstname, lastname, department, salary, email) VALUES
	('Vasya', 'Miller', 'IT', 68000.00, 'vasyamiller9@mail.com')
	RETURNING employeeid
	)
	
	INSERT INTO employeeprojects (employeeid, projectid, hoursworked)
	SELECT 
		ne.employeeid,
		p.projectid,
		80
	FROM new_employee ne
	CROSS JOIN projects p 
	WHERE p.projectname = 'Website Redesign';
COMMIT;

--Checking transaction
SELECT e.firstname, e.lastname, p.projectname, ep.hoursworked
FROM employeeprojects ep
JOIN employees e ON ep.employeeid = e.employeeid
JOIN projects p ON ep.projectid = p.projectid
WHERE e.firstname = 'Vasya';