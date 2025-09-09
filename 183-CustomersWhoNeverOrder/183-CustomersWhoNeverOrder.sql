-- Last updated: 09/09/2025, 14:19:41
# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT c.name AS Customers
FROM Customers c LEFT  JOIN  Orders o
On c.id=o.CustomerID
WHERE  o.id IS NULL