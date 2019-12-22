# Write your MySQL query statement below
select a.product_id product_id, round(sum(a.units*b.price)/sum(a.units),2) average_price
from UnitsSold a, Prices b 
where a.product_id=b.product_id and b.start_date<=a.purchase_date and a.purchase_date<= b.end_date
group by a.product_id
