CREATE SCHEMA SCHOOL;
USE SCHOOL;

CREATE TABLE courses (
course_id VARCHAR (10) PRIMARY KEY,
course_name TEXT,
fee INTEGER,
teacher TEXT
);

INSERT INTO courses VALUES
('C1','Data Analytics',15000,'Mr. Rao'),
('C2','Web Development',12000,'Ms. Fernandes'),
('C3','Machine Learning',20000,'Dr. Iyer'),
('C4','Cloud Basics',10000,'Mr. Khan');

CREATE TABLE students (
student_id INTEGER PRIMARY KEY,
name TEXT,
city TEXT,
age INTEGER,
course_id TEXT,
marks INTEGER,
admission_date DATE
);
INSERT INTO students VALUES
(1,'Aarav','Chennai',19,'C1',78,'2026-01-10'),
(2,'Meera','Mumbai',21,'C2',91,'2026-01-15'),
(3,'Rahul','Chennai',20,'C1',55,'2026-02-02'),
(4,'Sana','Delhi',22,'C3',88,'2026-02-11'),
(5,'John','Mumbai',19,'C2',64,'2026-03-05'),
(6,'Priya','Chennai',23,'C3',95,'2026-03-19'),
(7,'Kabir','Delhi',20,'C1',41,'2026-04-01'),
(8,'Divya','Mumbai',21,NULL,72,'2026-04-14'),
(9,'Arjun','Delhi',24,'C2',83,'2026-05-02'),
(10,'Nisha','Chennai',18,'C3',67,'2026-05-20');

SELECT name, city, marks FROM students;
SELECT * FROM students;


SELECT name, marks FROM students WHERE marks > 80;
SELECT * FROM students WHERE city = 'Chennai' AND age < 21;
SELECT * FROM students WHERE city IN ('Delhi','Mumbai');
SELECT * FROM students WHERE name LIKE 'A%'; 
SELECT * FROM students WHERE course_id IS NULL; 

SELECT name, marks FROM students ORDER BY marks DESC LIMIT 3;

SELECT COUNT(*), AVG(marks), MIN(marks), MAX(marks), SUM(marks)
FROM students;

SELECT city, COUNT(*) AS students, ROUND(AVG(marks),2) AS avg_marks
FROM students
GROUP BY city;


