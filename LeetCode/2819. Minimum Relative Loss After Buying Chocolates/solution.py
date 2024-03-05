class Solution: 
    def minimumRelativeLosses(self, prices: List[int], queries: List[List[int]]) -> List[int]:
        def fun(preLen: int) -> int:
            """从prices的前缀中选择preLen个数时,损失的最小值."""
            sufLen = count - preLen
            return preSum[preLen] + (2 * threshold * sufLen - sufSum[sufLen])

        def minimize(func, lo, hi):
            while lo < hi:
                m1 = lo+(hi-lo)//3
                m2 = hi-(hi-lo)//3
                if func(m1) >= func(m2):
                    lo = m1+1
                else:
                    hi = m2-1
            return func(lo) 


        prices.sort()
        preSum = [0] + list(accumulate(prices))
        sufSum = [0] + list(accumulate(prices[::-1]))
        res = [0] * len(queries)
        for i, (threshold, count) in enumerate(queries):
            res[i] = minimize(fun, 0, count)
        return res

# 作者：草莓奶昔🍓
# 链接：https://leetcode.cn/problems/minimum-relative-loss-after-buying-chocolates/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。