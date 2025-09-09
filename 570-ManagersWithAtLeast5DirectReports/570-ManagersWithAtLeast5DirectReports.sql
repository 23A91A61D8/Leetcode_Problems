-- Last updated: 09/09/2025, 14:19:13
# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN Employee m ON e.id = m.managerId
GROUP BY e.id
HAVING COUNT(m.id) >= 5;
