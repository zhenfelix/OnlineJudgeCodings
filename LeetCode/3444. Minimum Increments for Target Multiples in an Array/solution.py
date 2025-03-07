class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        # 预处理 target 的所有子集的 LCM
        m = len(target)
        lcms = [1] * (1 << m)
        for i, t in enumerate(target):
            bit = 1 << i
            for mask in range(bit):
                lcms[bit | mask] = lcm(t, lcms[mask])

        @cache
        def dfs(i: int, j: int) -> int:
            if j == 0:
                return 0
            if i < 0:  # 不能有剩余元素
                return inf
            # 不修改 nums[i]
            res = dfs(i - 1, j)
            # 枚举 j 的所有非空子集 sub，把 nums[i] 改成 lcms[sub] 的倍数
            sub = j
            while sub:
                l = lcms[sub]
                res = min(res, dfs(i - 1, j ^ sub) + (l - nums[i] % l) % l)
                sub = (sub - 1) & j
            return res
        return dfs(len(nums) - 1, (1 << m) - 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-increments-for-target-multiples-in-an-array/solutions/3061806/zi-ji-zhuang-ya-dpji-yi-hua-sou-suo-di-t-aeaj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# import math
# from math import gcd
# from functools import reduce

# def lcm(a, b):
#     return a * b // gcd(a, b) if a and b else 0

# def lcm_list(numbers):
#     return reduce(lcm, numbers, 1)

# class Solution:
#     def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
#         k = len(target)
#         full_mask = (1 << k) - 1
        
#         # Precompute LCM for all non-empty subsets of target
#         lcm_map = {}
#         for mask in range(1, 1 << k):
#             elements = [target[i] for i in range(k) if (mask & (1 << i))]
#             current_lcm = elements[0]
#             for num in elements[1:]:
#                 current_lcm = lcm(current_lcm, num)
#             lcm_map[mask] = current_lcm
        
#         # Initialize DP
#         dp = [float('inf')] * (1 << k)
#         dp[0] = 0
        
#         for x in nums:
#             new_dp = dp.copy()
#             for mask in lcm_map:
#                 lcm_val = lcm_map[mask]
#                 steps = (lcm_val - x % lcm_val) % lcm_val
#                 # Iterate through all possible current masks
#                 for current_mask in range(1 << k):
#                     if dp[current_mask] + steps < new_dp[current_mask | mask]:
#                         new_dp[current_mask | mask] = min(new_dp[current_mask | mask], dp[current_mask] + steps)
#             dp = new_dp
        
#         return dp[full_mask] if dp[full_mask] != float('inf') else -1









