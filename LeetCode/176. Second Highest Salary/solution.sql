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