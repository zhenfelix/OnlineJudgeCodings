# Write your MySQL query statement below
select sum(TIV_2016) TIV_2016
from 
insurance a 
left join
(select TIV_2015, count(*) cnt1 from insurance group by TIV_2015) b on a.TIV_2015=b.TIV_2015
left join
(select LAT, LON, count(*) cnt2 from insurance group by LAT,LON) c on a.LAT=c.LAT and a.LON=c.LON
where b.cnt1>1 and c.cnt2=1

-- SELECT
--     SUM(insurance.TIV_2016) AS TIV_2016
-- FROM
--     insurance
-- WHERE
--     insurance.TIV_2015 IN
--     (
--       SELECT
--         TIV_2015
--       FROM
--         insurance
--       GROUP BY TIV_2015
--       HAVING COUNT(*) > 1
--     )
--     AND CONCAT(LAT, LON) IN
--     (
--       SELECT
--         CONCAT(LAT, LON)
--       FROM
--         insurance
--       GROUP BY LAT , LON
--       HAVING COUNT(*) = 1
--     )
-- ;


-- -- 作者：LeetCode
-- -- 链接：https://leetcode-cn.com/problems/investments-in-2016/solution/2016nian-de-tou-zi-by-leetcode/
-- -- 来源：力扣（LeetCode）
-- -- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。