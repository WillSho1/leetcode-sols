# Problem: Rising Temperature
# Goal: Master self-joins and date comparison logic.

/* TODO: Find all dates' Id with higher temperatures compared to its previous dates (yesterday) */

SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate)=1
WHERE w1.temperature > w2.temperature;