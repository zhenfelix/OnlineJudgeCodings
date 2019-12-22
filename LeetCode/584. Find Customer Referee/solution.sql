# Write your MySQL query statement below
-- SELECT name FROM customer WHERE referee_id <> 2 OR referee_id IS null;

-- SELECT 
--   NAME 
-- FROM
--   customer 
-- WHERE id NOT IN 
--   (SELECT 
--     id 
--   FROM
--     customer 
--   WHERE referee_id = 2)


-- 作者：dong-fang-xu-ri
-- 链接：https://leetcode-cn.com/problems/find-customer-referee/solution/in-zi-cha-xun-by-dong-fang-xu-ri/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。