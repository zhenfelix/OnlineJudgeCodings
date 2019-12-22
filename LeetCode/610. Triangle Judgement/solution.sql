-- # Write your MySQL query statement below
-- select x,y,z,if(x+y>z and y+z>x and z+x>y,"Yes","No") triangle
-- from triangle

select *,
if((x + y <= z or x + z <= y or y + z <= x), "No", "Yes") as triangle
from triangle;


-- 作者：doublez
-- 链接：https://leetcode-cn.com/problems/triangle-judgement/solution/ifyu-ju-jian-ji-you-mei-li-by-doublez/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。