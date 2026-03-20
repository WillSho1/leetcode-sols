# Operations: SadServers Scenario - "Tokyo"

Scenario Focus: SSH Troubleshooting

## Instructions
1. Navigate to: https://sadservers.com/scenario/tokyo
2. Scenario: Someone messed up the SSH configuration. You need to fix it.
3. Diagnose the issue using local terminal and logs.

## Commands & Findings
(Document your investigation below)

- Check SSH service status: `systemctl status ssh`
- Check logs: `journalctl -u ssh -n 20`
- Config Test: `sshd -t`
- ...

## Resolution
(How did you solve it?)
It seems you have the wrong problem, this was about serving an html file. Anyways, I curled localhost, and it says it was 403 forbidden. I figured this had to do with the file permissions so I checked and it was 600, so I changes it to 644 (rw-r--r--). It seems that the firewall was dropping http connections too in iptables, I did not know how to check this before and had to use the clues. iptables -F removed the rule I think.