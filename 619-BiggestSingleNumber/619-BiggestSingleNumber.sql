-- Last updated: 09/09/2025, 14:18:52
# Write your MySQL query statement below
SELECT MAX(num) AS num 
FROM MyNumbers
WHERE num IN (
    SELECT num FROM MyNumbers 
    GROUP BY num 
    HAVING COUNT(num) = 1
);

