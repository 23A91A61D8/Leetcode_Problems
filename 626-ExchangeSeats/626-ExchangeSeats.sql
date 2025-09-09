-- Last updated: 09/09/2025, 14:18:49
# Write your MySQL query statement below

SELECT id,
CASE
    WHEN MOD(id,2) = 1 THEN LEAD(student,1,student)OVER(ORDER BY id)
    ELSE LAG(student,1) OVER(ORDER BY id)
END AS student
FROM seat;
