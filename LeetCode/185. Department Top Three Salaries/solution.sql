# Write your MySQL query statement below

# select d.Name as Department, e1.Name as Employee, e1.Salary as Salary
# from Employee e1, Department d
# where e1.DepartmentId = d.Id and 3 > (
#     select count(distinct Salary)
#     from Employee e2
#     where e1.DepartmentId = e2.DepartmentId and e2.Salary > e1.Salary
# )


select d.Name as Department, a.Name as Employee, a.Salary as Salary
from
(
    select Name,
    @num := if(@dpt_id=e.DepartmentId,if(@salary=e.Salary,@num,@num+1),1) num,
    @dpt_id := e.DepartmentId DepartmentId,
    @salary := e.Salary Salary
    from 
    (select @dpt_id := 0, @salary := 0, @num := 0) tmp,
    Employee e
    order by e.DepartmentId, e.Salary desc
) a, Department d
where a.DepartmentId = d.Id and num <= 3