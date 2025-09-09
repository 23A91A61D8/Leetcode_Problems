-- Last updated: 09/09/2025, 14:18:51
# Write your MySQL query statement below
SELECT * 
FROM Cinema
WHERE id % 2 = 1 -- Selects movies with an odd-numbered ID
AND description <> 'boring' -- Excludes movies with a "boring" description
ORDER BY rating DESC; -- Sorts results by rating in descending order
