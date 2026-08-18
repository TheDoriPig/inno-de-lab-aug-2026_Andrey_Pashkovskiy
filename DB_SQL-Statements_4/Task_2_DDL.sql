--Create new table
CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
Location VARCHAR(50)
);

--Add new column to the employees table
ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);

--Filled in the column Email
UPDATE Employees 
SET Email = LOWER(CONCAT(firstname, lastname, employeeid, '@mail.com'));

--Add constraint unique 
ALTER TABLE Employees ADD CONSTRAINT unique_email UNIQUE (Email);

--Rename column
ALTER TABLE Departments RENAME COLUMN Location TO OfficeLocation;