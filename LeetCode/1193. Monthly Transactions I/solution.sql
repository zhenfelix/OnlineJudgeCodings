# Write your MySQL query statement below

select
date_format(trans_date,'%Y-%m') as month,
country,
count(*) as trans_count,
-- sum(if(state='approved',1,0)) as approved_count,
sum(case when state = 'approved' then 1 else 0 end) as approved_count,
sum(amount) as trans_total_amount,
-- sum(if(state='approved',amount,0)) as approved_total_amount
sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions t
group by
month,country
