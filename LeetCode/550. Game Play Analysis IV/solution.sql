# Write your MySQL query statement below



-- select 
-- round(
-- (
-- select count(*)
-- from
-- (
-- select a.player_id
-- from 
-- (
-- select player_id, min(event_date) min_date
-- from Activity
-- group by player_id
-- ) a, Activity b 
-- where a.player_id=b.player_id and a.min_date+1=b.event_date
-- ) c 
-- )/count(distinct player_id)
-- ,2) fraction
-- from Activity


select round(sum(case when datediff(a.event_date,b.first_date)=1 then 1 else 0 end)/(select count(distinct(player_id)) from activity),2) as fraction
from activity a,
(select player_id,min(event_date) first_date from activity group by player_id) b
where a.player_id=b.player_id


-- 作者：rople-2
-- 链接：https://leetcode-cn.com/problems/game-play-analysis-iv/solution/fen-bu-zou-jie-du-xiang-xi-by-rople-2-2/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

