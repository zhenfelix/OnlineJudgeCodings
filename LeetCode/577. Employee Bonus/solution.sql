# Write your MySQL query statement below
select name, bonus from Employee a left join Bonus b on a.empId=b.empId where b.bonus is null or b.bonus<1000