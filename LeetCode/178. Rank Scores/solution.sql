# Write your MySQL query statement below
# select Score, Rank
# from
# (
# select Score,
# # @rank := @rank+(@s<>Score) Rank,
# @rank := if(@s=Score,@rank+0,@rank+1) Rank,
# @s := Score
# from Scores, (select @rank := 0, @s := -1) a
# order by Score desc
# ) tmp

# Write your MySQL query statement below

SELECT a.Score, COUNT(DISTINCT b.Score) AS `RANK`
FROM Scores a, Scores b
WHERE a.Score <= b.Score
GROUP BY a.Id
ORDER BY `RANK`;

select Score, Rank
from
(
select Score,
# @rank := @rank+(@s<>Score) Rank,
cast(@rank := if(@s=Score,@rank,@rank+1) as signed integer)  Rank,
@s := Score
from Scores, (select @rank := 0, @s := -1) a
order by Score desc
) tmp


# select score, @a := @a + (@pre <> (@pre := Score)) as rank 
# from scores,(select @a := 0, @pre := -1) t 
# order by score desc; 

# SELECT
#   Score,
#   @rank := @rank + (@prev <> (@prev := Score)) Rank
# FROM
#   Scores,
#   (SELECT @rank := 0, @prev := -1) init
# ORDER BY Score desc


# select a.Score Score, count(distinct b.Score) Rank
# from Scores a, Scores b
# where a.Score <= b.Score
# group by a.Id
# order by Score desc

 SELECT
   Score,
   (SELECT count(distinct Score) FROM Scores WHERE Score >= s.Score) Rank
 FROM Scores s
 ORDER BY Score desc

# select score, 
#        dense_rank() over(order by Score desc) as Rank
# from Scores;

# 作者：houziAI
# 链接：https://leetcode-cn.com/problems/rank-scores/solution/tu-jie-sqlmian-shi-ti-jing-dian-pai-ming-wen-ti-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。