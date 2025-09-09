-- Last updated: 09/09/2025, 14:18:56
SELECT 
  x, y, z,
  CASE 
    WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
    ELSE 'No'
  END AS triangle
FROM Triangle;
