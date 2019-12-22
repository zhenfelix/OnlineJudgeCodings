# Write your MySQL query statement below

select round(avg(rate)*100,2) average_daily_percent
from
(
select action_date, count(distinct b.post_id)/count(distinct a.post_id) rate
from Actions a 
left join Removals b 
on a.post_id=b.post_id
where action="report" and extra="spam"
group by action_date
) tmp 