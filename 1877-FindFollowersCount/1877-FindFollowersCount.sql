-- Last updated: 09/09/2025, 14:17:27
# Write your MySQL query statement below
# SELECT  user_id, follower_id as followers_count
SELECT user_id, COUNT(follower_id) AS followers_count
From Followers
Group By user_id
order by user_id;