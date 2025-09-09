-- Last updated: 09/09/2025, 14:19:46
# Write your MySQL query statement below
# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;