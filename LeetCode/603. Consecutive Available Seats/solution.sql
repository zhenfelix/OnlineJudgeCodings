-- # Write your MySQL query statement below

-- select seat_id
-- from cinema
-- where free = 1 and (seat_id+1 in (select seat_id from cinema where free = 1) or seat_id-1 in (select seat_id from cinema where free = 1))

select distinct a.seat_id
from cinema a join cinema b
  on abs(a.seat_id - b.seat_id) = 1
  and a.free = true and b.free = true
order by a.seat_id
;


-- 作者：LeetCode
-- 链接：https://leetcode-cn.com/problems/consecutive-available-seats/solution/lian-xu-kong-yu-zuo-wei-by-leetcode/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。