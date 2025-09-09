-- Last updated: 09/09/2025, 14:19:03
# Write your MySQL query statement below


SELECT class 
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
