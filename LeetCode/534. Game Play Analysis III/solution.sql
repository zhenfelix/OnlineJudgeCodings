# Write your MySQL query statement below
-- select a.player_id as player_id, a.event_date as event_date, sum(b.games_played) as games_played_so_far
-- from Activity a, Activity b 
-- where 
-- b.event_date <= a.event_date and b.player_id = a.player_id
-- group by a.player_id, a.event_date



select player_id, event_date, games_played_so_far
from
(
select
player_id,
event_date,
@cnt := if(@id = player_id, @cnt := @cnt+games_played, @cnt := games_played) games_played_so_far,
@id := player_id
from
Activity,
(select @cnt := 0, @id := 0) tmp
order by player_id, event_date
) tmp