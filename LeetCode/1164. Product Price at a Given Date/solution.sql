# Write your MySQL query statement below

-- select a.product_id,ifnull(b.new_price,10) as price
-- from
-- (select distinct product_id from Products) a left join
-- (select product_id,new_price from Products where (product_id,change_date) in (select product_id,max(change_date) as change_date from Products where change_date<='2019-08-16' group by product_id)) b
-- on a.product_id=b.product_id

-- 作者：ma-shi-fu-eric
-- 链接：https://leetcode-cn.com/problems/product-price-at-a-given-date/solution/bu-gua-yong-unionde-si-lu-by-ma-shi-fu-eric/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

SELECT * 
FROM 
(SELECT product_id, new_price AS price
 FROM Products
 WHERE (product_id, change_date) IN (
                                     SELECT product_id, MAX(change_date)
                                     FROM Products
                                     WHERE change_date <= '2019-08-16'
                                     GROUP BY product_id)

 UNION all

 SELECT DISTINCT product_id, 10 AS price
 FROM Products
 WHERE product_id NOT IN (SELECT product_id FROM Products WHERE change_date <= '2019-08-16')
) tmp
ORDER BY price DESC


-- 作者：Durant
-- 链接：https://leetcode-cn.com/problems/product-price-at-a-given-date/solution/mysqljie-fa-shi-yong-union-by-durant/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。