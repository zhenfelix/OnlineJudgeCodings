# Write your MySQL query statement below
-- select a.Name as Name 
-- from Employee a, Employee b 
-- where a.Id = b.ManagerId
-- group by a.Id 
-- having count(b.Id) >= 5

-- SELECT
--     NAME
-- FROM
--     Employee
-- WHERE
--     Id IN (
--         SELECT
--             ManagerId
--         FROM
--             Employee e
--         GROUP BY
--             ManagerId
--         HAVING
--             ManagerId != 'null'
--         AND count(ManagerId) >= 5
--     )


    -- 第一步的结果作为临时表，然后join
    SELECT
        e1. NAME AS NAME
    FROM
        Employee AS e1
    JOIN (
        SELECT
            ManagerId
        FROM
            Employee e
        GROUP BY
            ManagerId
        HAVING
            ManagerId != 'null'
        AND count(ManagerId) >= 5
    ) AS e2 ON e1.Id = e2.ManagerId


    -- -- 自连接过滤
    -- SELECT
    --     e1. NAME
    -- FROM
    --     Employee AS e1
    -- JOIN Employee AS e2 ON (e1.id = e2.managerid)
    -- GROUP BY
    --     e1.id
    -- HAVING
    --     count(e1.id) >= 5
