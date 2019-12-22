-- # Write your MySQL query statement below
-- select tmp.seller_id
-- from 
-- (
--  select seller_id, sum(price) as total
--  from Sales S 
--  group by seller_id
-- ) tmp
-- right join
-- (
--     select max(tmp.total) as maxtotal
--     from 
--     (
--      select seller_id, sum(price) as total
--      from Sales S 
--      group by seller_id
--     ) tmp 
-- ) mx 
-- on tmp.total = mx.maxtotal

-- select seller_id 
-- from 
-- Sales 
-- group by 
-- seller_id 
-- having 
-- sum(price) = (select sum(price) as ye_ji from  Sales  group by  seller_id order by ye_ji desc limit 1);

select 
seller_id
from sales
group by seller_id
having
sum(price)>=all(select sum(price) from sales group by seller_id )