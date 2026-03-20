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
