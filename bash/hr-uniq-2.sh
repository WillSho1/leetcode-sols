# Problem: Uniq - 2
# Goal: Master `uniq -c` and basic output formatting.

# TODO: Read from stdin, count consecutive occurrences, and clean up the output
uniq -c | sed 's/^ *//'