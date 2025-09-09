-- Last updated: 09/09/2025, 14:19:11

SELECT 
  E.name,
  B.bonus
FROM 
  Employee E
LEFT JOIN 
  Bonus B
ON 
  E.empId = B.empId
WHERE 
  B.bonus < 1000 OR B.bonus IS NULL;
