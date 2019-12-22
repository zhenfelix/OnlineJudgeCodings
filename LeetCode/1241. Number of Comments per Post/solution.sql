# Write your MySQL query statement below


-- SELECT b.sub_id as post_id, count(distinct a.sub_id) as number_of_comments
-- FROM Submissions a 
-- right join 
-- (SELECT distinct sub_id
-- FROM Submissions
-- where parent_id is null) b 
-- on b.sub_id = a.parent_id
-- group by b.sub_id
-- order by b.sub_id


-- SELECT b.post_id, count(distinct a.sub_id) as number_of_comments
-- FROM 
-- (SELECT distinct sub_id as post_id
-- FROM Submissions
-- where parent_id is null) b 
-- left join 
-- Submissions a 
-- on b.post_id = a.parent_id
-- group by b.post_id


SELECT
    post_id,
    COUNT( DISTINCT S2.sub_id ) AS number_of_comments 
FROM
    ( SELECT DISTINCT sub_id AS post_id FROM Submissions WHERE parent_id IS NULL ) S1
    LEFT JOIN Submissions S2 ON S1.post_id = S2.parent_id 
GROUP BY S1.post_id
