select a.visited_on visited_on, sum(b.amount) amount, round(sum(b.amount)/7,2) average_amount
from (select distinct visited_on from Customer) a, Customer b 
where datediff(a.visited_on,b.visited_on) < 7 and datediff(a.visited_on,b.visited_on) >= 0
group by visited_on
LIMIT 18446744073709551610 OFFSET 6