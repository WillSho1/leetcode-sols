SELECT employee_id,
    CASE
        WHEN SUBSTRING(name, 1, 1) = "M" OR employee_id%2 = 0 THEN 0
        ELSE salary
    END AS bonus
FROM Employees
ORDER BY employee_id;

sed
`s/old/new/` substitution in sed.
uniq -c | sed 's/^ *//'
sed 's/\bthe\b/this/'

process tools
| Tool  | What it is               | When to use it                                                                                                                                                                |
| ----- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| top   | Standard "Task Manager"  | Use for a quick, "bare-bones" look at what's eating your CPU/RAM right now. (Available on every Linux server by default).                                                     |
| htop  | Interactive task manager | Use this 90% of the time. It’s color-coded, lets you scroll, and allows you to "kill" processes by just highlighting them and pressing F9. Much more human-friendly than top. |
| ps    | Process Snapshot         | Use when you want a "one-shot" list of everything running (e.g., ps aux). It's static, not live. Great for piping into grep.                                                  |
| pgrep | Process search           | Use when you just want the PID (Process ID) of a specific program. Instead of `ps aux                                                                                         |

cross join
SELECT stu.student_id, stu.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students stu
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON e.student_id=stu.student_id AND e.subject_name=sub.subject_name
GROUP BY stu.stude_id, sub.subject_name
ORDER BY stu.student_id, sub.subject_name;


AWK
awk '{
    if ($2>=50 && $3>=50 && $4>=50) {
        pf = "Pass"
    }
    else {
        pf = "Fail"
    }
    { print $1 " : " pf }
}'

ternary
awk '{
    pf = ($2>=50 && $3>=50 && $4>=50) ? "Pass" : "Fail"
    print $1 ":" pf
}'

It seems you have the wrong problem, this was about serving an html file. Anyways, I curled localhost, and it says it was 403 forbidden. I figured this had to do with the file permissions so I checked and it was 600, so I changes it to 644 (rw-r--r--). It seems that the firewall was dropping http connections too in iptables, I did not know how to check this before and had to use the clues. iptables -F removed the rule I think.
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content)>15;

IFNULL, AVG, BETWEEN
SELECT p.product_id, IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id=u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

DATE_SUB, INTERVAL
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date;

python string.find('char', start, end) -> index


SELECT query_name,
    ROUND(SUM(rating/position)/COUNT(*), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)/COUNT(*)*100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;

truncating sql month - can be used in select/group by
DATE_FORMAT(date_column, '%Y-%m')

example:
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(CASE WHEN state='approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state='approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country;