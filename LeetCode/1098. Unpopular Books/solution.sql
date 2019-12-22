-- select book_id, name
-- from Books
-- where available_from <= date("2019-05-23") and 
-- book_id not in (select book_id from Orders where dispatch_date >= date("2018-06-23") group by book_id having sum(quantity) >= 10)

select t1.book_id,t1.name from 
(select * from books where available_from <date_sub('2019-06-23',interval 1 Month)) t1 
left join 
(select *,(case when dispatch_date between '2018-06-23' and '2019-06-23' then quantity else 0 end) num from orders)  t2 
on t1.book_id=t2.book_id 
group by t1.book_id 
having sum(if(t2.num is null,0,t2.num))<10


-- 作者：RyanJin
-- 链接：https://leetcode-cn.com/problems/unpopular-books/solution/kan-ying-wen-fan-yi-zhong-wen-fan-yi-shao-liao-ju-/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。