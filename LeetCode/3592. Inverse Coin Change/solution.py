# class Solution:
#     def findCoins(self, numWays: List[int]) -> List[int]:
#         n = len(numWays)
#         ans = []
#         @lru_cache(None)
#         def dfs(i,t):
#             if t == 0:
#                 return 1
#             if i < 0:
#                 return 0 
#             cnt = dfs(i-1,t)
#             if t-ans[i] >= 0:
#                 cnt += dfs(i,t-ans[i])
#             return cnt
#         for v, w in enumerate(numWays):
#             if w > 0:
#                 cnt = dfs(len(ans)-1,v+1)
#                 if w == cnt+1:
#                     ans.append(v+1)
#                 elif w == cnt:
#                     continue
#                 else:
#                     return []
#             else:
#                 cnt = dfs(len(ans)-1,v+1)
#                 if 0 != cnt:
#                     return []
#         return ans 

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        mx = max(numWays)
        n = len(numWays)
        f = [1] + [0] * n
        ans = []
        for i, ways in enumerate(numWays, 1):
            if ways == f[i]:
                continue
            if ways - 1 != f[i]:
                return []
            ans.append(i)
            # 现在得到了一个大小为 i 的物品，用 i 计算完全背包（空间优化写法）
            for j in range(i, n + 1):
                f[j] += f[j - i]
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/inverse-coin-change/solutions/3705647/wan-quan-bei-bao-pythonjavacgo-by-endles-y6oq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。