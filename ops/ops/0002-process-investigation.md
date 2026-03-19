# Ops Drill: Process & Resource Observation

## Task
Investigate a "mysterious" high-load local system. Practice using foundational observation tools.

## Reference
- Missing Semester (CLI Tools): https://missing.csail.mit.edu/2020/command-line/

## Investigation Log
1. **Tool:** `top` / `htop`
   - Goal: Identify the top 3 CPU-consuming processes.
   - Findings:

2. **Tool:** `ps` / `pgrep`
   - Goal: Find the PID of a specific background process (e.g., your terminal or a browser).
   - Findings:

3. **Tool:** `journalctl` / `dmesg`
   - Goal: Check the last 10 lines of the system log for any hardware or kernel alerts.
   - Findings:

## Reflection
- Why is `htop` generally preferred over `top` for interactive debugging?
- What are the 'zombie' processes (Z state)?
