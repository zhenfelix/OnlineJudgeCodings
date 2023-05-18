# Write your MySQL query statement below

select

    employee_id,

    salary * (

        employee_id&1 and substr(name, 1, 1)<>'M'

    ) as bonus

from employees

order by employee_id;

# 作者：ykaitao
# 链接：https://leetcode.cn/problems/calculate-special-bonus/solutions/970020/mysql-7chong-jie-fa-by-ykaitao-3kc0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。