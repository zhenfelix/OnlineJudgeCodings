from typing import List, Tuple, Optional
from collections import defaultdict, Counter
from sortedcontainers import SortedList

MOD = int(1e9 + 7)
INF = int(1e20)

# 我们认为当销售员同一天推销的产品数目大于 8 个的时候，那么这一天就是「成功销售的一天」。
# 所谓「销售出色区间」，意味在这段时间内，「成功销售的天数」是严格 大于「未成功销售的天数」。
# 请你返回「销售出色区间」的最大长度。


class Solution:
    def longestESR(self, sales: List[int]) -> int:
        pre = dict({0: -1})
        res = cursum = 0

        for i, h in enumerate(sales):
            cursum += 1 if h > 8 else -1
            if cursum > 0:
                res = i + 1
            if cursum - 1 in pre:
                res = max(res, i - pre[cursum - 1])
            pre.setdefault(cursum, i)
        return res

class Solution:
    def longestESR(self, sales: List[int]) -> int:
        sales = [1 if s > 8 else -1 for s in sales]
        n = len(sales)
        ans = 0
        presums = [0]
        for s in sales:
            presums.append(presums[-1]+s)
        st = [0]
        for i in range(1,n+1):
            s = presums[i]
            if s < presums[st[-1]]:
                st.append(i)
        # print(sales,presums,st)
        for i in range(1,n+1)[::-1]:
            s = presums[i]
            while st and presums[st[-1]] < s:
                j = st.pop()
                ans = max(ans, i-j)
        return ans
