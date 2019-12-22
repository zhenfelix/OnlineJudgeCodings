# Write your MySQL query statement below

-- select Id, Company, Salary
-- from Employee a
-- where (select count(*) from Employee where Company = a.Company and Salary <= a.Salary) >= (select count(*) from Employee where Company = a.Company and Salary > a.Salary) and (select count(*) from Employee where Company = a.Company and Salary >= a.Salary) >= (select count(*) from Employee where Company = a.Company and Salary < a.Salary)

-- select Id, Company, Salary
-- from 
-- (
-- select cast(@rank:=if(@com=Company,@rank+1,1) as signed integer) Rank, Id, @com:=Company Company, Salary
-- from Employee, (select @rank:=0, @com:=null) a 
-- order by Company, Salary
-- ) b 
-- where Rank = floor(((select count(*) from Employee where Company=b.Company)+1)/2) or 
-- Rank = floor(((select count(*) from Employee where Company=b.Company)+2)/2)

select Id, b.Company, Salary
from 
(
select cast(@rank:=if(@com=Company,@rank+1,1) as signed integer) Rank, Id, @com:=Company Company, Salary
from Employee, (select @rank:=0, @com:=null) a 
order by Company, Salary
) b, 
(
select Company, floor((count(*)+1)/2) md1, floor((count(*)+2)/2) md2 from Employee group by Company
) c
where b.Company=c.Company and (b.Rank=c.md1 or b.Rank=c.md2)

-- select b.id,b.company,b.salary
-- -- 3. 连接结果
-- from (
--     -- 1. 按 company 分组排序，记为 `rk`
--     select id,company,salary,
--     case @com when company then @rk:=@rk+1 else @rk:=1 end rk,
--     @com:=company
--     from employee,(select @rk:=0, @com:='') a
--     order by company,salary) b
-- left join 
--     (-- 2. 计算各 company 的记录数除以2，记为 `cnt`
--     select company,count(1)/2 cnt from employee group by company) c
-- on b.company=c.company
-- -- 4. 找出符合中位数要求的记录
-- where b.rk in (cnt+0.5,cnt+1,cnt);
-- -- 觉得有用请不吝点个赞哟


-- 作者：chenhao1
-- 链接：https://leetcode-cn.com/problems/median-employee-salary/solution/chao-guo-99-de-mysql-jie-fa-by-chenhao1/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。