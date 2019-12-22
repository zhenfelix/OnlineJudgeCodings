# Write your MySQL query statement below
select a.follower follower, count(b.followee) num
from (select distinct follower from follow) a, (select distinct followee, follower from follow) b 
where a.follower=b.followee
group by follower 
order by follower 