--Create function to calculate annual bonus
CREATE FUNCTION CalculateAnnualBonus(
	p_employee_id INT,
	p_salary NUMERIC 
)
RETURNS NUMERIC 
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN p_salary * 0.10;
END;
$$;

--Use thise function
SELECT employeeid, firstname, lastname, salary, 
       CalculateAnnualBonus(employeeid, salary) AS annual_bonus
FROM Employees;

--Create VIEW to select all employees from IT department
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT employeeid, firstname, lastname, salary
FROM Employees
WHERE department = 'IT';

--Use thise VIEW
SELECT * FROM IT_Department_View;
