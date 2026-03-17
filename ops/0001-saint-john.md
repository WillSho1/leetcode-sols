# 0001-saint-john.md
## Operational Mastery: Saint John (The Memory Hog)

### Scenario
A process is consuming a massive amount of memory, but it's not showing up clearly in `top`. 

### Task
1. Use `strace`, `lsof`, and `/proc` to identify the rogue process.
2. Link: https://sadservers.com/scenario/saint-john

### Commands & Findings Log
- **Observation:**
I did not know the commands to use, but I started with empty lsof and got a huge list. I then tailed the log to see what was happening. I didn't entirely know what lsof output, so I looked it up and it told me to use lsof | grep /var/log/bad.log. I also learned about lsof and that I could just do lsof /var/log/bad.log and then pkill -9 PID.
- **Debugging Steps:**

- **Resolution:**
