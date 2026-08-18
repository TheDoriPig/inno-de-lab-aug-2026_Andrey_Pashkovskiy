--Tests for Task 3
SELECT * FROM Employees;

INSERT INTO Employees (FirstName, LastName, Department, Salary, Email) VALUES
('Ivan', 'Miller', 'HR', 70000.00, 'ivanmiller8@mail.com');

UPDATE Employees
SET salary = 65000.00
WHERE firstname = 'Ivan';