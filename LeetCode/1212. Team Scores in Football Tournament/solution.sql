-- # Write your MySQL query statement below
select Teams.team_id team_id, team_name, sum(if(num_points,num_points,0)) num_points
from
Teams
left join
(
(
    select host_team team_id, case when host_goals>guest_goals then 3 when host_goals=guest_goals then 1 else 0 end num_points
    from
    Matches
) 
union all
(
    select guest_team team_id, case when host_goals<guest_goals then 3 when host_goals=guest_goals then 1 else 0 end num_points
    from
    Matches
) 
) tmp
on Teams.team_id=tmp.team_id
group by Teams.team_id, team_name
order by num_points desc, Teams.team_id

