# Write your MySQL query statement below
-- select round(sum(if(order_date=customer_pref_delivery_date,1,0))/count(*),4)*100 immediate_percentage
-- from
-- (
--     select customer_id, min(order_date) order_date, min(customer_pref_delivery_date) customer_pref_delivery_date
--     from Delivery 
--     group by customer_id
-- ) tmp

select round(count(
    case when d.order_date = d.customer_pref_delivery_date then 1
    end
) * 100/count(*),2) as immediate_percentage
from Delivery d,
(select delivery_id,customer_id,min(order_date) as order_date
from Delivery
group by customer_id) as t
where d.customer_id = t.customer_id and d.order_date = t.order_date


-- 作者：couchpotato613
-- 链接：https://leetcode-cn.com/problems/immediate-food-delivery-ii/solution/mysqlshi-xian-by-couchpotato613-2/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。