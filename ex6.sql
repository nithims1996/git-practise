USE SCHOOL;
SELECT name,marks
from students

SELECT *  FROM students
WHERE city='chennai' AND age BETWEEN 18 and 20;

SELECT * FROM students
WHERE course_id IS NULL

SELECT name,marks
FROM students
ORDER BY marks DESC
LIMIT 3;

SELECT city, COUNT(*) as count of students
FROM students
GROUP BY CITY

SELECT city,ROUND(AVG(marks),2)AS avg_marks
FROM students
GROUP BY city
ORDER BY avg_marks DESC;

