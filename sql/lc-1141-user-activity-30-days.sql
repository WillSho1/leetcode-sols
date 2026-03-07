-- LeetCode 1141: User Activity for the Past 30 Days I
-- Category: Aggregates (SQL Tier 2)
-- Difficulty: Easy (Good for Aggregate/Date practice)

/*
Problem: Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on some day if they made at least one activity on that day.

Table: Activity
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
*/

SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
WHERE 
    activity_date > '2019-06-27' AND activity_date <= '2019-07-27'
GROUP BY 
    activity_date;

-- Explanation:
-- 1. Filters activity between 2019-06-28 and 2019-07-27 (the 30-day window).
-- 2. Groups results by date to get daily counts.
-- 3. Counts DISTINCT user_id because a user can have multiple activities in a single day.
