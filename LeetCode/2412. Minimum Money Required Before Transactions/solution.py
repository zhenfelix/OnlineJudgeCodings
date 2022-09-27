class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_lose = mx = 0
        for cost, cashback in transactions:
            total_lose += max(cost - cashback, 0)
            mx = max(mx, min(cost, cashback))
        return total_lose + mx


作者：endlesscheng
链接：https://leetcode.cn/problems/minimum-money-required-before-transactions/solution/by-endlesscheng-lvym/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        s = sum(a-b for a, b in transactions if a > b)
        ans = 0
        for a, b in transactions:
            delta = s 
            if a > b:
                delta -= (a-b)
            ans = max(ans, a+delta)
        return ans 