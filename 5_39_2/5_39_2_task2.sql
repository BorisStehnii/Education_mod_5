--1
SELECT first_name as 'First Name', last_name as 'Last Name' FROM employees;
--2
SELECT  DISTINCT  department_id FROM employees ORDER BY department_id; 
--3
SELECT * FROM employees ORDER BY first_name DESC;
--4
SELECT first_name, last_name, salary, salary*0.12 as PF FROM employees;
--5
SELECT MAX(salary) as mas_salary, MIN(salary) as min_salary FROM employees;
--6
SELECT first_name, last_name, salary, ROUND(salary/CAST(12 AS REAL), 2) as 'monthly  salary' FROM employees;
