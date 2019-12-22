# Write your MySQL query statement below



-- select *
-- from
-- (
-- select a.spend_date spend_date, "desktop" platform, sum(if(b.platform="desktop",a.amount,0)) total_amount, count(distinct if(b.platform="desktop",a.user_id,null)) total_users
-- from Spending a
-- left join
-- (select user_id, spend_date, if(count(distinct platform)=2,"both",platform) platform from Spending group by user_id, spend_date) b 
-- on a.user_id=b.user_id and a.spend_date=b.spend_date
-- group by spend_date

-- union all

-- select a.spend_date spend_date, "mobile" platform, sum(if(b.platform="mobile",a.amount,0)) total_amount, count(distinct if(b.platform="mobile",a.user_id,null)) total_users
-- from Spending a
-- left join
-- (select user_id, spend_date, if(count(distinct platform)=2,"both",platform) platform from Spending group by user_id, spend_date) b 
-- on a.user_id=b.user_id and a.spend_date=b.spend_date
-- group by spend_date

-- union all 

-- select a.spend_date spend_date, "both" platform, sum(if(b.platform="both",a.amount,0)) total_amount, count(distinct if(b.platform="both",a.user_id,null)) total_users
-- from Spending a
-- left join
-- (select user_id, spend_date, if(count(distinct platform)=2,"both",platform) platform from Spending group by user_id, spend_date) b 
-- on a.user_id=b.user_id and a.spend_date=b.spend_date
-- group by spend_date
-- ) tmp
-- order by spend_date


select c.spend_date spend_date, c.platform platform, sum(if(d.amount,d.amount,0)) total_amount, count(distinct d.user_id) total_users
from
(
select distinct spend_date, state platform from Spending,
(
    select "desktop" state 
    union all 
    select "mobile" state 
    union all 
    select "both" state
) tmp
) c left join 
(
select a.spend_date spend_date, b.platform platform, amount, a.user_id user_id
from Spending a
left join
(select user_id, spend_date, if(count(distinct platform)=2,"both",platform) platform from Spending group by user_id, spend_date) b 
on a.user_id=b.user_id and a.spend_date=b.spend_date
) d 
on c.spend_date=d.spend_date and c.platform=d.platform
group by spend_date, platform
-- order by spend_date, if(c.platform="mobile",1,if(c.platform="desktop",2,3))
order by c.spend_date, field(c.platform,'desktop','mobile','both')

-- select p1.spend_date, p1.platform, (if(t3.spend_date is null,0,t3.tmount)) as total_amount,
--     if(t3.spend_date is null, 0, t3.tusers) as total_users from 
--    (
--     select t2.spend_date, p.platform from 
--     (select distinct spend_date from Spending) t2
--         join 
--         (
--             select 'desktop' as platform 
--             union all
--             select 'mobile' as platform
--             union all
--             select 'both' as platform 
--         )p 
--    )p1 left join 
--     (
--         select  spend_date, platform, sum(amount) as tmount, count(user_id) as tusers from
--         ( 
--         select spend_date, user_id,
--         (
--             case when count(platform)>1 then 'both'
--                  else platform 
--             end
--         ) as platform,
--         sum(amount) as amount 
--         from Spending 
--         group by spend_date, user_id
--         )t1 group by spend_date, platform
--     )t3   on p1.spend_date=t3.spend_date and p1.platform=t3.platform
