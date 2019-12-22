# Write your MySQL query statement below
SELECT IFNULL(ROUND(AVG(session_count), 2), 0) AS average_sessions_per_user
FROM (
SELECT user_id,
       COUNT(DISTINCT session_id) as session_count
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) <= 29
GROUP BY user_id) TMP
