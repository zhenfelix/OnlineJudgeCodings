# Write your MySQL query statement below


select min(round(sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2)),2)) shortest
from point_2d a, point_2d b 
where not (a.x=b.x and a.y=b.y)