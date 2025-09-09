-- Last updated: 09/09/2025, 14:17:47
# Write your MySQL query statement below
SELECT 
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM 
    Activities
GROUP BY 
    sell_date
ORDER BY 
    sell_date;
