-- Last updated: 09/09/2025, 14:17:31
# Write your MySQL query statement below
# SELECT * FROM Users
SELECT user_id, 
       CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
