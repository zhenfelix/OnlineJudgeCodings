# Write your MySQL query statement below

-- SELECT IFNULL(
-- (
-- SELECT DISTINCT Salary 
-- FROM Employee
-- ORDER BY Salary DESC
-- LIMIT 1 OFFSET 1
-- )
-- ,NULL)
-- AS SecondHighestSalary

# Write your MySQL query statement below

-- SELECT
--     (SELECT DISTINCT
--             Salary
--         FROM
--             Employee
--         ORDER BY Salary DESC
--         LIMIT 1 OFFSET 1) AS SecondHighestSalary
-- ;


select max(Salary) SecondHighestSalary
from Employee
where Salary < (select max(Salary) from Employee );



# Write your MySQL query statement below
select (
  select distinct Salary from Employee order by Salary Desc limit 1 offset 1
)as SecondHighestSalary