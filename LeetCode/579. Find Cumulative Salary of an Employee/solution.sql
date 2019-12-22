# Write your MySQL query statement below

select b.Id Id, b.Month Month, sum(c.Salary) Salary
from
(
select *
from Employee a
where Month!=(select max(Month) from Employee where Id=a.Id)
) b, Employee c
where b.Id=c.Id and b.Month-c.Month >= 0 and b.Month-c.Month <= 2
group by b.Id, b.Month
order by Id, Month desc
