CREATE TABLE students(
StudentId PRIMARY KEY,
NameStudent text not null,
PhoneNumber integer not null,
email text);

--1
ALTER TABLE students
RENAME TO StudentsUniversity;
--2
ALTER TABLE StudentsUniversity 
RENAME COLUMN email TO EmailStudent;
--3
INSERT INTO StudentsUniversity (NameStudent, PhoneNumber, EmailStudent) VALUES ('Boris', 3800050030, 'bor@gmail.com');
--4
INSERT INTO StudentsUniversity (NameStudent, PhoneNumber, EmailStudent) VALUES ('Denis', 38066005, 'den@gmail.com');
--5
UPDATE StudentsUniversity
SET PhoneNumber = 38099999
WHERE NameStudent = 'Boris';
--6
DELETE FROM StudentsUniversity
WHERE NameStudent = 'Denis';

