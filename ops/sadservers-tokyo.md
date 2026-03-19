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
