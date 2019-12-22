# Write your MySQL query statement below
select d.Name Department, e.Name Employee, e.Salary Salary
from
Employee e, Department d
where e.DepartmentId = d.Id and 
e.Salary = (select max(Salary) from Employee where DepartmentId=e.DepartmentId)