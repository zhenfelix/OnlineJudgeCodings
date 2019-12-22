# Write your MySQL query statement below

-- select p.project_id project_id, p.employee_id employee_id
--     from 
--     Project p, Employee e,
--     (
--     select project_id, max(experience_years) mx 
--     from 
--     Project p, Employee e 
--     where p.employee_id=e.employee_id
--     group by project_id
-- ) tmp
-- where p.employee_id=e.employee_id and p.project_id=tmp.project_id and e.experience_years=tmp.mx

select p.project_id, p.employee_id
from Project p
join Employee e
on p.employee_id = e.employee_id
where (p.project_id, e.experience_years) in (
select p.project_id,max(e.experience_years)
from project p join employee e on p.employee_id = e.employee_id
group by p.project_id )

-- 作者：jayce-11
-- 链接：https://leetcode-cn.com/problems/project-employees-iii/solution/yong-yi-zu-xin-xi-jin-xing-pi-pei-by-jayce-11/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。