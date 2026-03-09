-- Reference: https://www.hackerrank.com/challenges/average-population-of-each-continent/
-- Topic: SQL Aggregates/Joins - Tier 2 SQL
-- Goal: Query the names of all the continents (COUNTRY table) and their respective average city populations (CITY table) rounded down to the nearest integer.

SELECT ctry.CONTINENT, FLOOR(AVG(cty.POPULATION))
FROM COUNTRY ctry
JOIN CITY cty ON cty.COUNTRYCODE=ctry.CODE
GROUP BY ctry.CONTINENT;