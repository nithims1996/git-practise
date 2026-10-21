USE SCHOOL;


SELECT city ,ROUND(AVG(marks),2)AS AVG_MARK
FROM students
GROUP BY city
HAVING AVG(marks)>72;

SELECT s.name,c.course_name, c.fee
FROM students s
INNER JOIN courses c ON s.course_id=c.course_id;


SELECT c.course_name, COUNT(s.student_id) AS total_students
FROM courses c
LEFT JOIN students s ON c.course_id = s.course_id
GROUP BY c.course_name;

SELECT name, marks,
CASE WHEN marks >= 85 THEN 'A'
WHEN marks >= 70 THEN 'B'
ELSE 'C' END AS grade
FROM students
ORDER BY marks DESC;
