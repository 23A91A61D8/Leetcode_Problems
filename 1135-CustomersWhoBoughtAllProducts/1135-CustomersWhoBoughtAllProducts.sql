-- Last updated: 09/09/2025, 14:18:40
# Write your MySQL query statement below
-- LeetCode 1045: Customers Who Bought All Products

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
