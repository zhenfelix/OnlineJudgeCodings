# Write your MySQL query statement below

-- select distinct a.product_id , b.product_name
-- from Sales a 
-- join Product b 
-- on a.product_id = b.product_id
-- where sale_date>='2019-01-01' and sale_date<='2019-03-31'
-- and a.product_id not in 
-- (select product_id
-- from Sales
-- where sale_date<'2019-01-01' or sale_date>'2019-03-31'
-- )

select  a.product_id
        , Product.product_name
from 
(
    select      distinct    product_id
    from        Sales
    where       sale_date>=date('2019-01-01')
    and         sale_date<=date('2019-03-31')
)a 
left join 
(
    select      distinct    product_id
    from        Sales
    where       sale_date<date('2019-01-01')
    or         sale_date>date('2019-03-31')
)b
on  a.product_id = b.product_id
left join Product 
on  Product.product_id = a.product_id
where   b.product_id is null 

-- select a.product_id , b.product_name
-- from Sales a 
-- join Product b 
-- on a.product_id = b.product_id
-- group by a.product_id
-- having min(a.sale_date) >= "2019-01-01" and max(a.sale_date) <= "2019-03-31"



-- where sale_date between str_to_date("01/01/2019","%d/%m/%Y") and str_to_date("01/03/2019","%d/%m/%Y") 