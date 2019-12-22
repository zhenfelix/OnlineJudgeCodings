# Write your MySQL query statement below
-- select b.event_date install_dt, count(b.event_date) installs, round(sum(if(c.event_date and datediff(c.event_date,b.event_date)=1,1,0))/count(*),2) Day1_retention
-- from
-- (select player_id, event_date
-- from Activity a 
-- where 0 = (select count(*) from Activity where player_id=a.player_id and event_date<a.event_date)) b
-- left join
-- (select player_id, event_date
-- from Activity a 
-- where 1 = (select count(*) from Activity where player_id=a.player_id and event_date<a.event_date)) c
-- on b.player_id=c.player_id
-- group by b.event_date

-- select b.event_date install_dt, count(b.event_date) installs, round(count(c.event_date)/count(b.event_date),2) Day1_retention
-- from
-- (select player_id, event_date
-- from Activity a 
-- where 0 = (select count(*) from Activity where player_id=a.player_id and event_date<a.event_date)) b
-- left join
-- Activity c
-- on b.player_id=c.player_id and c.event_date=b.event_date+1
-- group by b.event_date

select b.event_date install_dt, count(b.event_date) installs, round(count(c.event_date)/count(b.event_date),2) Day1_retention
from
(select player_id, min(event_date) event_date
from Activity a 
group by player_id) b
left join
Activity c
on b.player_id=c.player_id and c.event_date=b.event_date+1
group by b.event_date