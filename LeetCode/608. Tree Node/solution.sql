# Write your MySQL query statement below
-- select id, case when p_id is null then "Root" when id in (select distinct p_id from tree) then "Inner" else "Leaf" end Type
-- from tree

SELECT
    atree.id,
    IF(ISNULL(atree.p_id),
        'Root',
        IF(atree.id IN (SELECT p_id FROM tree), 'Inner','Leaf')) Type
FROM
    tree atree
ORDER BY atree.id


-- 作者：LeetCode
-- 链接：https://leetcode-cn.com/problems/tree-node/solution/shu-jie-dian-by-leetcode/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。