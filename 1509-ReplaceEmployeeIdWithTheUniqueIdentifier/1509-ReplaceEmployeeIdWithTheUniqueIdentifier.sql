-- Last updated: 09/09/2025, 14:17:52
# Write your MySQL query statement below
SELECT 
    euni.unique_id,
    e.name
FROM 
    Employees e
LEFT JOIN 
    EmployeeUNI euni
ON 
    e.id = euni.id;
