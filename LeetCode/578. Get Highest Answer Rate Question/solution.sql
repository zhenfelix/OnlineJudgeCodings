# Write your MySQL query statement below

SELECT 
    question_id AS 'survey_log'
FROM
    survey_log
GROUP BY question_id
ORDER BY COUNT(answer_id) / sum(IF(action = 'show', 1, 0)) DESC
LIMIT 1;


-- 作者：LeetCode
-- 链接：https://leetcode-cn.com/problems/get-highest-answer-rate-question/solution/cha-xun-hui-da-lu-zui-gao-de-wen-ti-by-leetcode/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。