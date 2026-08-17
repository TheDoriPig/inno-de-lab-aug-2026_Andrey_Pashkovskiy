SELECT 
	p.projectname 
FROM projects p 
JOIN employeeprojects ep ON p.projectid = ep.projectid
JOIN employees e ON ep.employeeid = e.employeeid 
WHERE e.firstname = 'Bob' AND e.lastname = 'Johnson' AND ep.hoursworked > 150;

--------------------------------------------------------------------------------

UPDATE projects p 
SET Budget = Budget * 1.10
WHERE EXISTS (
	SELECT 1
	FROM employeeprojects ep
	JOIN employees e ON ep.employeeid = e.employeeid 
	WHERE ep.projectid = p.projectid AND e.department = 'IT'
);

SELECT p.projectid, p.projectname, p.budget 
FROM projects p;

--------------------------------------------------------------------------------

UPDATE projects 
SET enddate = NULL
WHERE projectid = 4;

UPDATE projects
SET enddate = startdate + INTERVAL '1 year'
WHERE enddate IS NULL 

SELECT p.projectid, p.projectname, p.startdate, p.enddate 
FROM projects p 

--------------------------------------------------------------------------------

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
ROLLBACK;

SELECT e.firstname, e.lastname, p.projectname, ep.hoursworked
FROM employeeprojects ep
JOIN employees e ON ep.employeeid = e.employeeid
JOIN projects p ON ep.projectid = p.projectid
WHERE e.firstname = 'Vasya';