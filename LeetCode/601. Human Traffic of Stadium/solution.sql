# Write your MySQL query statement below

# select c.id id, c.visit_date visit_date, c.people people
# from
# (
# select a.*, @state:=if(people>=100,1,-1) state, @rank:=if(@state=@pre,@rank,@rank+1) rank, @pre:=@state pre
# from stadium a, (select @rank:=0,@state:=null,@pre:=null) b
# ) c,
# (
# select * from
#     (
#         select a.*, @state2:=if(people>=100,1,-1) state, @rank2:=if(@state2=@pre2,@rank2,@rank2+1) rank, @pre2:=@state2 pre
#         from stadium a, (select @rank2:=0,@state2:=null,@pre2:=null) b
#     ) tmp
# where state=1
# group by rank
# having count(*)>=3
# ) d
# where c.rank=d.rank
# order by visit_date

SELECT s1.* FROM stadium AS s1, stadium AS s2, stadium as s3
    WHERE 
    ((s1.id + 1 = s2.id
    AND s1.id + 2 = s3.id)
    OR 
    (s1.id - 1 = s2.id
    AND s1.id + 1 = s3.id)
    OR
    (s1.id - 2 = s2.id
    AND s1.id - 1 = s3.id)
    )
    AND s1.people>=100 
    AND s2.people>=100
    AND s3.people>=100

    GROUP BY s1.id