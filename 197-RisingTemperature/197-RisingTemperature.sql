-- Last updated: 09/09/2025, 14:19:35
# Write your MySQL query statement below
SELECT w1.id 
FROM Weather w1
JOIN Weather w2 
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
