class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        @lru_cache(None)
        def f(i, mask):
            if i < 0:
                return 0
            t, w, res = mask, 1, 0
            for k in range(1, numSlots + 1):
                if t % 3:
                    res = max(res, f(i-1, mask-w) + (k & nums[i]))
                t, w = t // 3, w * 3
            return res
        
        return f(len(nums) - 1, 3**numSlots-1)


# 作者：newhar
# 链接：https://leetcode-cn.com/problems/maximum-and-sum-of-array/solution/san-jin-zhi-zhuang-tai-ya-suo-by-newhar-t3fe/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        dp = [[-float('inf')]*(3**numSlots) for i in range(n+1)]
        dp[0][0] = 0
        def getstate(s):
            states = []
            for j in range(numSlots):
                states.append(s%3)
                s //= 3
            return states

        for i in range(n):
            for s in range(3**numSlots):
                if dp[i][s] == -float('inf'):
                    continue
                states = getstate(s)
                for j in range(numSlots):
                    if states[j] < 2:
                        ns = s+(3**(j))
                        dp[i+1][ns] = max(dp[i+1][ns], dp[i][s]+((j+1)&nums[i]))
        return max(dp[n])



class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        ps = [1]
        for _ in range(numSlots):
            ps.append(ps[-1]*3)
        dp = [-float('inf') for i in range(ps[numSlots])]
        dp[0] = 0
        def getstate(s):
            states = []
            for j in range(numSlots):
                states.append(s%3)
                s //= 3
            return states

        for i in range(n):
            for s in range(ps[numSlots])[::-1]:
                if dp[s] == -float('inf'):
                    continue
                states = getstate(s)
                for j in range(numSlots):
                    if states[j] < 2:
                        ns = s+ps[j]
                        dp[ns] = max(dp[ns], dp[s]+((j+1)&nums[i]))
        return max(dp)


# TLE
# class Solution:
#     def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
#         n = len(nums)
#         dp = [-float('inf') for i in range(1<<n)]
#         dp[0] = 0

#         for i in range(numSlots):
#             for s in range(1<<n)[::-1]:
#                 if dp[s] == -float('inf') or bin(s).count('1')+(numSlots-i)*2<n:
#                     continue
#                 for j in range(n):
#                     if (s>>j)&1:
#                         continue
#                     ns = s|(1<<j)
#                     dp[ns] = max(dp[ns], dp[s]+(nums[j]&(i+1)))
#                     for k in range(j+1,n):
#                         if (s>>k)&1:
#                             continue
#                         ns = s|(1<<j)|(1<<k)
#                         dp[ns] = max(dp[ns], dp[s]+(nums[j]&(i+1))+(nums[k]&(i+1)))
#         return dp[-1]


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        f = [0] * (1 << (numSlots * 2))
        for i, fi in enumerate(f):
            c = i.bit_count()
            if c >= len(nums):
                continue
            for j in range(numSlots * 2):
                if (i & (1 << j)) == 0:  # 枚举空篮子 j
                    s = i | (1 << j)
                    f[s] = max(f[s], fi + ((j // 2 + 1) & nums[c]))
        return max(f)


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/maximum-and-sum-of-array/solution/zhuang-tai-ya-suo-dp-by-endlesscheng-5eqn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。