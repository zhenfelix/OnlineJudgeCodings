# Write your MySQL query statement below

-- select distinct page_id recommended_page
-- from Likes a,
-- ((select user2_id user_id from Friendship where user1_id=1) union (select user1_id user_id from Friendship where user2_id=1)) tmp
-- where page_id not in (select page_id from Likes where user_id=1) and a.user_id=tmp.user_id

select distinct page_id as recommended_page
from Likes,friendship
where page_id
not in
(select page_id from likes where user_id=1)
and
( user_id in (select user1_id from friendship where user2_id=1)
or
user_id in (select user2_id from friendship where user1_id=1));

-- 作者：anquan
-- 链接：https://leetcode-cn.com/problems/page-recommendations/solution/1264ye-mian-tui-jian-by-anquan/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。