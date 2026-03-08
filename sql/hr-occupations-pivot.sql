# [SQL] SQL Window Functions: ROW_NUMBER(), RANK(), DENSE_RANK()

- **URL:** https://www.hackerrank.com/challenges/occupations/problem
- **Focus:** SQL Advanced Operations (Tier 2/3)
- **Status:** ⏳ Pending

## Problem Statement
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL if there are no more names corresponding to an occupation.

## Key Concept
Use `ROW_NUMBER()` with `PARTITION BY` and `CASE` statements to perform this dynamic pivot.
