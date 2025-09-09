-- Last updated: 09/09/2025, 14:18:17
SELECT person_name
FROM (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_weight, turn
    FROM Queue
) AS cumulative_weights
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
