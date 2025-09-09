-- Last updated: 09/09/2025, 14:18:37
# Write your MySQL query statement below
SELECT 
    p.product_name, 
    s.year, 
    s.price
FROM 
    Sales s
JOIN 
    Product p 
ON 
    s.product_id = p.product_id;
