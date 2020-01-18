# Write your MySQL query statement below

select a.gender gender, a.day day, sum(b.score_points) total
from Scores a, Scores b 
where a.gender = b.gender and a.day >= b.day 
group by gender, day
order by gender, day