# [Bash] Sed & Awk: Text Processing Pipeline

- **URL:** https://www.hackerrank.com/challenges/text-processing-in-linux-the-sed-command-1/
- **Focus:** Linux Tooling (Tier 2/3)
- **Status:** ⏳ Pending

## Problem Statement
For each line in a given input file, transform all occurrences of the first 'the' into 'this'. Ensure the search is case-insensitive.

## Key Concept
Use `sed 's/.../.../i'` or `awk` to perform conditional replacement. Experiment with regex capturing groups.

## Input Example
Input: The quick brown fox jumps over the lazy dog.
Output: this quick brown fox jumps over the lazy dog.
