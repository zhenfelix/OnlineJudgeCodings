# Write your MySQL query statement below

select group_id, player_id
from
(
select group_id, a.player_id player_id, sum(if(points,points,0)) points
from
Players a left join (
    (
        select first_player player_id, first_score points
        from Matches
    )
    union all
    (
        select second_player player_id, second_score points
        from Matches
    )
) b
on a.player_id=b.player_id
group by a.player_id
order by points desc, player_id
) tmp
group by group_id


-- # Write your MySQL query statement below

-- select group_id,player_id from 
-- (select group_id,player_id,sum((
--     case when player_id = first_player then first_score
--          when player_id = second_player then second_score
--          end
-- )) as totalScores
-- from Players p,Matches m
-- where p.player_id = m.first_player
-- or p.player_id = m.second_player
-- group by player_id
-- order by totalScores desc,player_id) as temp
-- group by group_id

-- -- 作者：couchpotato613
-- -- 链接：https://leetcode-cn.com/problems/tournament-winners/solution/guan-lian-cha-xun-jia-shang-fen-zu-pai-xu-by-couch/
-- -- 来源：力扣（LeetCode）
-- -- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。