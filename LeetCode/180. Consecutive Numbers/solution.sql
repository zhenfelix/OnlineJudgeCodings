# Write your MySQL query statement below

# select distinct Num ConsecutiveNums
# from
# (
# select @rank:=if(@pre=Num,@rank,@rank+1) rank, @pre:=Num Num from Logs, (select @rank:=0, @pre:=null) tmp
# ) a
# group by rank
# having count(*) >= 3

Select DISTINCT l1.Num ConsecutiveNums from Logs l1, Logs l2, Logs l3 
where l1.Id=l2.Id-1 and l2.Id=l3.Id-1 
and l1.Num=l2.Num and l2.Num=l3.Num