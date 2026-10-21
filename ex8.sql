USE SCHOOL;

SELECT strftime('%m', admission_date) AS month, COUNT(*)
FROM students GROUP BY month; 


SELECT UPPER(name), LENGTH(name) FROM students;
SELECT COALESCE(course_id, 'Not enrolled') FROM students;