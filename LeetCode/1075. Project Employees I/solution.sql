# Write your MySQL query statement below

-- select project_id, round(avg(experience_years),2) as average_years
-- from
-- (
--     select project_id, experience_years
--     from Project p join Employee e 
--     on p.employee_id = e.employee_id
-- ) tmp
-- group by project_id

select project_id ,round(avg(experience_years),2) as average_years
from Project
left join Employee
on Project.employee_id = Employee.employee_id
group by project_id
order by project_id;
