-- Last updated: 09/09/2025, 14:17:12
# Write your MySQL query statement below
SELECT
teacher_id,
COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id


