# Write your MySQL query statement below


select ss.student_id as student_id, ss.student_name as student_name, ss.subject_name as subject_name, count(e.student_id) as attended_exams
from 
(
    select * from Students, Subjects
) ss left join Examinations e 
on ss.student_id = e.student_id and ss.subject_name = e.subject_name
group by ss.student_id, ss.subject_name