# Write your MySQL query statement below
-- select buyer_id
-- from Product p, Sales s 
-- where p.product_id=s.product_id
-- group by s.buyer_id
-- having sum(p.product_name='S8') > 0 and sum(p.product_name='iPhone')=0

select distinct buyer_id
from product p inner join sales s
on p.product_id=s.product_id
where product_name='S8' 
and (buyer_id not in (
select buyer_id
from product p inner join sales s
on p.product_id=s.product_id
    where product_name='iPhone')
     )

-- 作者：soyguapa
-- 链接：https://leetcode-cn.com/problems/sales-analysis-ii/solution/not-in-zuo-lian-jie-by-soyguapa/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。