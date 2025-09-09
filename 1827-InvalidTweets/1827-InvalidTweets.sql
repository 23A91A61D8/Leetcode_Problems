-- Last updated: 09/09/2025, 14:17:29
# Write your MySQL query statement below

SELECT tweet_id 
FROM Tweets
WHERE LENGTH(content) > 15;
