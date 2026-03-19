# Problem: Calculate Special Bonus
# Goal: Master `IF` or `CASE WHEN` logic in SQL.

/* 
TODO: Calculate bonus for each employee.
Bonus is 100% of salary if:
1. ID is odd
2. Name does not start with 'M'
Otherwise, bonus is 0.
*/
SELECT employee_id,
    CASE
        WHEN SUBSTRING(name, 1, 1) = "M" OR employee_id%2 = 0 THEN 0
        ELSE salary
    END AS bonus
FROM Employees
ORDER BY employee_id;