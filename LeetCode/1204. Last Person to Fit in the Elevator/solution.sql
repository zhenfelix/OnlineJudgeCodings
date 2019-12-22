# Write your MySQL query statement below

-- select person_name
-- from
-- Queue
-- where turn = (select max(turn) from 
-- (
-- select 
-- person_name,
-- turn,
-- @total := weight+@total t 
-- from Queue,
-- (select @total := 0) tmp
-- order by turn    
-- ) new_q
-- where t <= 1000)


select person_name
from Queue q1
where (select sum(weight) from Queue where turn <= q1.turn) <= 1000
order by turn desc limit 1
