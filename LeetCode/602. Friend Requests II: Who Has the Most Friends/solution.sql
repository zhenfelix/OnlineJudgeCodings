# Write your MySQL query statement below

-- select requester_id id, count(*) num
-- from
-- (
--     (select requester_id, accepter_id from request_accepted)
--     union
--     (select accepter_id requester_id, requester_id accepter_id from request_accepted)
-- ) tmp
-- group by requester_id
-- order by num desc
-- limit 1

select ids as id, cnt as num
from
(
select ids, count(*) as cnt
   from
   (
        select requester_id as ids from request_accepted
        union all
        select accepter_id from request_accepted
    ) as tbl1
   group by ids
   ) as tbl2
order by cnt desc
limit 1
;


-- 作者：LeetCode
-- 链接：https://leetcode-cn.com/problems/friend-requests-ii-who-has-the-most-friends/solution/hao-you-shen-qing-ii-shui-you-zui-duo-de-hao-you-b/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。