# Write your MySQL query statement below
select state period_state, min(dt) start_date, max(dt) end_date
from
(
select a.*, @rank:=if(@pre=state,@rank,@rank+1) rank, @pre:=state
from
(
    select fail_date dt, "failed" state from Failed 
    union all 
    select success_date dt, "succeeded" state from Succeeded
) a, (select @rank:=0,@pre:=null) tmp
where dt >= "2019-01-01" and dt <= "2019-12-31"
order by dt 
) b 
group by rank