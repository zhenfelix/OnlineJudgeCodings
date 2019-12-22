# Write your MySQL query statement below
select dept_name, count(student_id) student_number
from 
department a left join student b 
on a.dept_id=b.dept_id
group by a.dept_id
order by student_number desc, dept_name