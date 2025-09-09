-- Last updated: 09/09/2025, 14:19:43
# Write your MySQL query statement below
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
