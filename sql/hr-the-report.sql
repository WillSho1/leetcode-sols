-- Reference: https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
-- Topic: SQL Joins/Aggregates - Tier 2 SQL
-- Goal: Query the name, grade, and marks for students. If grade < 8, name = NULL. Sort by Grade DESC, Name ASC, Marks ASC.

SELECT 
    CASE
        WHEN g.Grade < 8 THEN NULL
        ELSE s.Name
    END AS name,
    g.Grade, s.Marks
FROM Students s
LEFT JOIN Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC,
    CASE
        WHEN g.Grade < 8 THEN s.Marks
        ELSE name
    END ASC;
