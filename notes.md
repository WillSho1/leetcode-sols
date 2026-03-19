SELECT employee_id,
    CASE
        WHEN SUBSTRING(name, 1, 1) = "M" OR employee_id%2 = 0 THEN 0
        ELSE salary
    END AS bonus
FROM Employees
ORDER BY employee_id;

`s/old/new/` substitution in sed.
uniq -c | sed 's/^ *//'
sed 's/\bthe\b/this/'


| Tool  | What it is               | When to use it                                                                                                                                                                |
| ----- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| top   | Standard "Task Manager"  | Use for a quick, "bare-bones" look at what's eating your CPU/RAM right now. (Available on every Linux server by default).                                                     |
| htop  | Interactive task manager | Use this 90% of the time. It’s color-coded, lets you scroll, and allows you to "kill" processes by just highlighting them and pressing F9. Much more human-friendly than top. |
| ps    | Process Snapshot         | Use when you want a "one-shot" list of everything running (e.g., ps aux). It's static, not live. Great for piping into grep.                                                  |
| pgrep | Process search           | Use when you just want the PID (Process ID) of a specific program. Instead of `ps aux                                                                                         |
