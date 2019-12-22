# Write your MySQL query statement below
select a.first_login_date login_date, count(*) user_count
from
(
select user_id, min(activity_date) first_login_date
from Traffic
where activity="login"
group by user_id
) a 
where datediff("2019-06-30",a.first_login_date)<=90
group by login_date