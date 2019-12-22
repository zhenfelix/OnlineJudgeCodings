# Write your MySQL query statement below

select a.log_id as START_ID ,min(b.log_id) as END_ID from 
(select log_id from logs where log_id-1 not in (select * from logs)) a,
(select log_id from logs where log_id+1 not in (select * from logs)) b
where b.log_id>=a.log_id
group by a.log_id

-- 作者：ma-shi-fu-eric
-- 链接：https://leetcode-cn.com/problems/find-the-start-and-end-number-of-continuous-ranges/solution/jian-yi-fang-fa-zhao-dao-lian-xu-zhi-de-tou-he-wei/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Write your MySQL query statement below

select min(log_id) start_id, max(log_id) end_id
from
(
select log_id, @rank:=if(@pre!=log_id-1,@rank+1,@rank+0) rank, @pre:=log_id pre 
from Logs, (select @pre:=null, @rank:=0) a
) b 
group by rank 