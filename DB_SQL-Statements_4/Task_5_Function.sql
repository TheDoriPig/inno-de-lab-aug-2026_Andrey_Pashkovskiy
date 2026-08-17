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

SELECT employeeid, firstname, lastname, salary, 
       CalculateAnnualBonus(employeeid, salary) AS annual_bonus
FROM Employees;

CREATE OR REPLACE VIEW IT_Department_View AS
SELECT employeeid, firstname, lastname, salary
FROM Employees
WHERE department = 'IT';

SELECT * FROM IT_Department_View;
