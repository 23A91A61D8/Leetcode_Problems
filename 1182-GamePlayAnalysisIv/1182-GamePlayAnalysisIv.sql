-- Last updated: 09/09/2025, 14:18:31
SELECT 
    ROUND(COUNT(DISTINCT a1.player_id) / COUNT(DISTINCT a2.player_id), 2) AS fraction
FROM 
    (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) a2
LEFT JOIN Activity a1
ON a1.player_id = a2.player_id 
AND DATEDIFF(a1.event_date, a2.first_login) = 1;
