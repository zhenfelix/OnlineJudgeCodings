class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        def dfs(i):
            nonlocal ans 
            if i*2+1 >= n:
                return
            dfs(i*2+1)
            dfs(i*2+2)
            l, r = cost[i*2+1], cost[i*2+2]
            ans += abs(l-r)
            cost[i] += max(l,r)
            return
        dfs(0)
        
        return ans


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2, 0, -1):  # 从最后一个非叶节点开始算
            ans += abs(cost[i * 2 - 1] - cost[i * 2])  # 两个子节点变成一样的
            cost[i - 1] += max(cost[i * 2 - 1], cost[i * 2])  # 累加路径和
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/solution/tan-xin-jian-ji-xie-fa-pythonjavacgo-by-5svh1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class Solution:
#     def minIncrements(self, n: int, cost: List[int]) -> int:
#         def dfs(i,pre):
#             if i >= n:
#                 return
#             cost[i] += pre 
#             dfs(i*2+1,cost[i])
#             dfs(i*2+2,cost[i])
#             return
#         dfs(0,0)
#         mx = max(cost)
#         # print(mx)
#         ans = 0
#         def dfs2(i):
#             nonlocal ans 
#             if i*2+1 >= n:
#                 return mx-cost[i]
#             left = dfs2(i*2+1)
#             right = dfs2(i*2+2)
#             mi = min(left,right)
#             ans += left+right-mi*2
#             # print(i,left,right,mi,ans)
#             return mi 
#         tmp = dfs2(0)
#         return ans+tmp


