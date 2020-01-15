# Write your MySQL query statement below
select a.employee_id employee_id, b.sz team_size
from Employee a, 
(
select team_id, count(distinct employee_id) sz
from Employee 
group by team_id
) b 
where a.team_id = b.team_id