# Write your MySQL query statement below
# select a.Name as Employee
# from 
# (
# select *
# from Employee 
# where ManagerId is not null
# ) a
# left join
# Employee b
# on a.ManagerId = b.Id
# where a.Salary > b.Salary

SELECT
    a.Name as Employee
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary
;


# select E.name as Employee from Employee E
# join Employee M
# on E.ManagerId = M.Id
# where E.Salary > M.Salary;