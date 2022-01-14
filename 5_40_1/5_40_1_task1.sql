--1
SELECT first_name, last_name, department_id, depart_name
FROM employees
JOIN departments
ON departments.department_id = employees.department_id;
--2
SELECT first_name, last_name, depart_name, city, state_province
FROM employees
JOIN departments
ON departments.department_id = employees.department_id
JOIN locations
ON locations.location_id = departments.location_id;
--3
SELECT first_name, last_name, department_id, depart_name
FROM employees
JOIN departments
ON departments.department_id = employees.department_id
WHERE departments.department_id = 40 or departments.department_id = 80;
--4
SELECT D.depart_name, (SELECT COUNT(E.department_id) FROM employees as E WHERE E.department_id = D.department_id) as workers
FROM departments as D;
--5
SELECT E.first_name, (SELECT first_name FROM employees WHERE employee_id = E.manager_id)
FROM employees as E;
--6
SELECT E.first_name, E.last_name, J.job_title, E.salary-J.max_salary
FROM employees as E
JOIN jobs as J
ON E.job_id = J.job_id;
--7
SELECT J.job_title, (SELECT AVG(E.salary) FROM employees as E WHERE E.job_id = J.job_id) 
FROM jobs as J;
--8
SELECT E.first_name, E.last_name, E.salary, L.city
FROM employees as E
JOIN department as D
ON D.department_id = E.department_id
JoIN locations L
ON L.location_id = D.location_id
WHERE L.city = 'London';
--9
SELECT D.depart_name, (SELECT COUNT(E.department_id) FROM employees as E WHERE E.department_id = D.department_id) as workers
FROM departments as D;
