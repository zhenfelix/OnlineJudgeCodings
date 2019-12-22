-- select month, country, approved_count, approved_amount, chargeback_count, chargeback_amount
-- from
-- (
-- select a.month month, a.country country, a.approved_count approved_count, a.approved_amount approved_amount, if(b.chargeback_count,b.chargeback_count,0) chargeback_count, if(b.chargeback_amount,b.chargeback_amount,0) chargeback_amount
-- from 
-- (
--     select LEFT (trans_date, 7) as month, country, sum(if(state="approved",1,0)) approved_count, sum(if(state="approved",amount,0)) approved_amount
--     from Transactions
--     group by LEFT (trans_date, 7), country
-- ) a
-- left join
-- (
--     select LEFT (Chargebacks.trans_date, 7) as month, country, count(*) chargeback_count, sum(amount) chargeback_amount
--     from Chargebacks left join Transactions
--     on Chargebacks.trans_id=Transactions.id 
--     group by LEFT (Chargebacks.trans_date, 7), country
-- ) b
-- on a.month=b.month and a.country=b.country

-- union 

-- select b.month month, b.country country, if(a.approved_count,a.approved_count,0) approved_count, if(a.approved_amount,a.approved_amount,0) approved_amount, b.chargeback_count chargeback_count, b.chargeback_amount chargeback_amount
-- -- select b.month, b.country, case when a.approved_count=null then 0 else a.approved_count end, case when a.approved_amount=null then 0 else a.approved_amount end, b.chargeback_count, b.chargeback_amount
-- from 
-- (
--     select LEFT (trans_date, 7) as month, country, sum(if(state="approved",1,0)) approved_count, sum(if(state="approved",amount,0)) approved_amount
--     from Transactions
--     group by LEFT (trans_date, 7), country
-- ) a
-- right join
-- (
--     select LEFT (Chargebacks.trans_date, 7) as month, country, count(*) chargeback_count, sum(amount) chargeback_amount
--     from Chargebacks left join Transactions
--     on Chargebacks.trans_id=Transactions.id 
--     group by LEFT (Chargebacks.trans_date, 7), country
-- ) b
-- on a.month=b.month and a.country=b.country
-- ) tmp
-- where not (approved_count=0 and approved_amount=0 and chargeback_count=0 and chargeback_amount=0)

-- select month, country,
--     sum(tag=0) as approved_count,
--     sum(IF(tag=0,amount,0)) as approved_amount,
--     sum(tag=1) as chargeback_count,
--     sum(case when tag=1 then amount else 0 end) as chargeback_amount from
-- (
-- select 1 as tag, country, amount, date_format(c.trans_date,'%Y-%m') month from ChargeBacks c 
--     left join Transactions on c.trans_id=Transactions.id
-- union all
-- select 0 as tag, country, amount, date_format(trans_date,'%Y-%m') month from Transactions
--     where state='approved'#去零
-- )t
-- group by month,country 
-- order by month, country

select month, country,
    sum(tag=0) as approved_count,
    sum(IF(tag=0,amount,0)) as approved_amount,
    sum(tag=1) as chargeback_count,
    sum(case when tag=1 then amount else 0 end) as chargeback_amount from
(
select 1 as tag, trans_id id, country, amount, date_format(c.trans_date,'%Y-%m') month from ChargeBacks c 
    left join Transactions on c.trans_id=Transactions.id
union
select 0 as tag, id, country, amount, date_format(trans_date,'%Y-%m') month from Transactions
    where state='approved'#去零
)t
group by month,country 
order by month, country