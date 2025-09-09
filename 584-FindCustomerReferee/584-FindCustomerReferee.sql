-- Last updated: 09/09/2025, 14:19:09
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;
