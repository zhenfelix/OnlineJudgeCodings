# Write your MySQL query statement below


-- select a.name America, b.name Asia, c.name Europe
-- from
-- (
--     select name, @rank:=@rank+1 rank from student, (select @rank:=0) tmp where continent="America" order by name
-- ) a left join
-- (
--     select name, @rank:=@rank+1 rank from student, (select @rank:=0) tmp where continent="Asia" order by name 
-- ) b on a.rank=b.rank 
-- left join 
-- (
--     select name, continent, @rank:=@rank+1 rank from student, (select @rank:=0) tmp where continent="Europe" order by name 
-- ) c on a.rank=c.rank

select a.name America, b.name Asia, c.name Europe
from
(
    select name, @rank1:=@rank1+1 rank from student, (select @rank1:=0) tmp where continent="America" order by name
) a left join
(
    select name, @rank2:=@rank2+1 rank from student, (select @rank2:=0) tmp where continent="Asia" order by name 
) b on a.rank=b.rank 
left join 
(
    select name, continent, @rank3:=@rank3+1 rank from student, (select @rank3:=0) tmp where continent="Europe" order by name 
) c on a.rank=c.rank 

-- select name, continent, @rank:=@rank+1 rank from student, (select @rank:=0) tmp where continent="Europe" order by name