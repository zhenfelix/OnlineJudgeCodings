# Write your MySQL query statement below

-- select max(num) as num
-- from
-- (
-- select num 
-- from my_numbers
-- group by num 
-- having count(*) = 1
-- ) tmp

select ifnull(
(SELECT *
FROM my_numbers
group by num
having count(*) = 1
order by num desc
limit 1),null) as num
