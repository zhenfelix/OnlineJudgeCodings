# Write your MySQL query statement below
-- select customer_id
-- from
-- (
--     select distinct customer_id, product_key from Customer 
-- ) tmp
-- group by customer_id
-- having sum(if(tmp.product_key in (select distinct product_key from Product),1,0))=(select count(distinct product_key) from Product)



select customer_id
from 
(select customer_id,count(distinct product_key) as num 
 from Customer
 group by customer_id
) t
join (
    select count(product_key) as num
    from Product
) m 
on t.num = m.num;


-- 作者：dong-fang-xu-ri
-- 链接：https://leetcode-cn.com/problems/customers-who-bought-all-products/solution/group-byyun-yong-by-dong-fang-xu-ri/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。