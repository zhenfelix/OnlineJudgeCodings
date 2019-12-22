# Write your MySQL query statement below
select project_id
from Project 
group by project_id
having count(*) = (select max(cc) from (select count(*) as cc from Project group by project_id) tmp)