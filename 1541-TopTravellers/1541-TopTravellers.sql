-- Last updated: 09/09/2025, 14:17:50
# Write your MySQL query statement below
SELECT u.name, 
       COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name ASC;
