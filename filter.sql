USE SCHOOL;

SELECT city, AVG(marks) AS avg_marks
FROM students
GROUP BY city
HAVING AVG(marks) > 72;

SELECT s.name, c.course_name, c.fee
FROM students s
INNER JOIN courses c ON s.course_id = c.course_id;

SELECT name, marks,
CASE WHEN marks >= 85 THEN 'A'
WHEN marks >= 70 THEN 'B'
ELSE 'C' END AS grade