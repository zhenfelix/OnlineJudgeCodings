# class Solution:
#     def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         n = len(nums)
#         @lru_cache(None)
#         def g(i,j):
#             if i == j: return nums[i]
#             return g(i+1,j)^g(i,j-1)
#         @lru_cache(None)
#         def f(i,j):
#             if i == j: return nums[i]
#             return max(g(i,j),f(i+1,j),f(i,j-1))
#         ans = []
#         for l, r in queries:
#             ans.append(f(l,r))
#         f.cache_clear()
#         g.cache_clear()
#         return ans 
class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            mx[i][i] = f[i][i] = nums[i]
            for j in range(i + 1, n):
                f[i][j] = f[i][j - 1] ^ f[i + 1][j]
                mx[i][j] = max(f[i][j], mx[i + 1][j], mx[i][j - 1])
        return [mx[l][r] for l, r in queries]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-xor-score-subarray-queries/solutions/2899932/qu-jian-dp-tao-qu-jian-dppythonjavacgo-b-w4be/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。