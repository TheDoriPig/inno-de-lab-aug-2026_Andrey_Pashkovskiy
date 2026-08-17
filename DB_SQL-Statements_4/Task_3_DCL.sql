CREATE USER hr_user WITH PASSWORD '123123';

GRANT USAGE ON SCHEMA hw_4 TO hr_user;
GRANT SELECT ON TABLE Employees TO hr_user;

GRANT INSERT, UPDATE ON Employees TO hr_user;

-- Без этого этих прав выдаёт ошибку при попытке добавить сотрудника
GRANT USAGE, SELECT, UPDATE ON SEQUENCE employees_employeeid_seq TO hr_user;