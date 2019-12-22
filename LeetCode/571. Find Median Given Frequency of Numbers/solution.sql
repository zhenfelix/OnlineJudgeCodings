# Write your MySQL query statement below

-- select (min(if(Cumulative>=(select floor((sum(Frequency)+1)/2) from Numbers),Number,null))+min(if(Cumulative>=(select floor((sum(Frequency)+2)/2) from Numbers),Number,null)))/2 median
-- from 
-- (
--     select Number, (select sum(Frequency) from Numbers where a.Number>=Number) Cumulative
--     from Numbers a
--     order by Number
-- ) tmp


-- select
-- avg(t.number) as median
-- from
-- (
-- select
-- n1.number,
-- n1.frequency,
-- (select sum(frequency) from numbers n2 where n2.number<=n1.number) as asc_frequency,
-- (select sum(frequency) from numbers n3 where n3.number>=n1.number) as desc_frequency
-- from numbers n1
-- ) t
-- where t.asc_frequency>= (select sum(frequency) from numbers)/2
-- and t.desc_frequency>= (select sum(frequency) from numbers)/2

-- 作者：ji-bai-4
-- 链接：https://leetcode-cn.com/problems/find-median-given-frequency-of-numbers/solution/jian-liang-ge-lei-ji-pin-lu-yong-yuan-gong-xin-shu/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

select avg(n.number) as median
from Numbers n
where n.Frequency >= abs((select sum(n2.Frequency) from Numbers n2 where n.number >= n2.number) - 
                        (select sum(n3.Frequency) from Numbers n3 where n.number <= n3.number))


-- https://zhuanlan.zhihu.com/p/47322393