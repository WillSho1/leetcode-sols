-- SQL: Average Population of Each Continent
-- URL: https://www.hackerrank.com/challenges/average-population-of-each-continent/
-- Tier 2 (Advanced Operations): aggregates

SELECT 
    COUNTRY.CONTINENT, 
    FLOOR(AVG(CITY.POPULATION))
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;
