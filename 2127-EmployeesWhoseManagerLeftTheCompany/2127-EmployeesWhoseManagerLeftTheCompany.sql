-- Last updated: 09/09/2025, 14:17:14
SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
ORDER BY e.employee_id;
