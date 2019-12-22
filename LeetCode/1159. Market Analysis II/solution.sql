# Write your MySQL query statement below

select d.user_id seller_id, if(c.item_brand is null or c.item_brand!=d.favorite_brand,"no","yes") 2nd_item_fav_brand
from Users d left join
(
select seller_id, item_brand
from
(
select seller_id, item_id
from
Orders a
where 1=(select count(*) from Orders where a.seller_id=seller_id and a.order_date>order_date)
) tmp left join Items
on tmp.item_id=Items.item_id
) c 
on d.user_id=c.seller_id
order by seller_id
