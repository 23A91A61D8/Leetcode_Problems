-- Last updated: 09/09/2025, 14:18:54
# Write your MySQL query statement below
SELECT name 
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT sales_id 
    FROM Orders 
    WHERE com_id = (SELECT com_id FROM Company WHERE name = 'RED')
);
