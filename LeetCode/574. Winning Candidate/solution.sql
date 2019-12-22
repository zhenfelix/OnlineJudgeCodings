# Write your MySQL query statement below
-- select Name 
-- from Candidate
-- where id in (
--     select CandidateId from Vote group by CandidateId having count(*)=
--     (
--         select max(cnt) from (select count(*) cnt from Vote group by CandidateId) tmp
--     )
--     -- (
--     --     select max(count(*)) from Vote group by CandidateId
--     -- )
-- )


select Name 
from Candidate a, (select CandidateId from Vote group by CandidateId order by count(*) desc limit 1) b
where a.id = b.CandidateId


