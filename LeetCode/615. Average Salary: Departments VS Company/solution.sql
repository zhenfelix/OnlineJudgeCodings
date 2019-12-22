# Write your MySQL query statement below
-- select c.pay_month pay_month, b.department_id department_id, if(round(sum(a.amount))=round(sum(c.total_month_pay)),"same",if(sum(a.amount)>sum(c.total_month_pay),"higher","lower")) comparison
-- from salary a,
-- employee b,
-- (
-- select left(pay_date,7) pay_month, avg(amount) total_month_pay
-- from salary
-- group by pay_month
-- ) c
-- where a.employee_id=b.employee_id and left(a.pay_date,7)=c.pay_month
-- group by c.pay_month, b.department_id

-- select c.pay_month pay_month, b.department_id department_id, round(sum(a.amount)), round(sum(c.total_month_pay))
-- from salary a,
-- employee b,
-- (
-- select left(pay_date,7) pay_month, avg(amount) total_month_pay
-- from salary
-- group by pay_month
-- ) c
-- where a.employee_id=b.employee_id and left(a.pay_date,7)=c.pay_month
-- group by c.pay_month, b.department_id


select department_salary.pay_month, department_id,
case
  when department_avg>company_avg then 'higher'
  when department_avg<company_avg then 'lower'
  else 'same'
end as comparison
from
(
  select department_id, avg(amount) as department_avg, date_format(pay_date, '%Y-%m') as pay_month
  from salary join employee on salary.employee_id = employee.employee_id
  group by department_id, pay_month
) as department_salary
join
(
  select avg(amount) as company_avg,  date_format(pay_date, '%Y-%m') as pay_month from salary group by date_format(pay_date, '%Y-%m')
) as company_salary
on department_salary.pay_month = company_salary.pay_month
;


-- 作者：LeetCode
-- 链接：https://leetcode-cn.com/problems/average-salary-departments-vs-company/solution/ping-jun-gong-zi-bu-men-yu-gong-si-bi-jiao-by-leet/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。