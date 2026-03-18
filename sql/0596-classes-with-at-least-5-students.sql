# Problem: Classes More Than 5 Students
# Goal: Master `GROUP BY` and `HAVING` for aggregate filtering.

/* TODO: Write your SQL query to find classes with at least 5 students */
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student)>=5;