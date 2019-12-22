# Write your MySQL query statement below
-- select b.player_id player_id, b.device_id device_id
-- from
-- (
--     select player_id, min(event_date) min_date
--     from Activity
--     group by player_id
-- ) a, Activity b 
-- where b.player_id=a.player_id and b.event_date=a.min_date

select a.player_id ,a.device_id from Activity a where (a.player_id ,a.event_date) in 
(select player_id,min(event_date) as first_login from Activity group by player_id)


-- 作者：rople-2
-- 链接：https://leetcode-cn.com/problems/game-play-analysis-ii/solution/inzi-cha-xun-by-rople-2/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。