class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        f = [(float("inf"), float("inf"))] * (1 << n)
        f[0] = (1, 0)

        def add(o: Tuple[int, int], x: int) -> Tuple[int, int]:
            if o[1] + x <= sessionTime:
                return o[0], o[1] + x
            return o[0] + 1, x
        
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    f[mask] = min(f[mask], add(f[mask ^ (1 << i)], tasks[i]))
        
        return f[(1 << n) - 1][0]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/solutions/966245/wan-cheng-ren-wu-de-zui-shao-gong-zuo-sh-tl0p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        cost = [0]*(1<<n)
        mp = {1<<i : i for i in range(n)}
        for s in range(1,1<<n):
            p = s-(s&-s)
            cost[s] = cost[p]+tasks[mp[s^p]]
        dp = [inf]*(1<<n)
        dp[0] = 0
        for s in range(1,1<<n):
            p = s 
            while p:
                # print(s,p)
                if cost[p] <= sessionTime: 
                    dp[s] = min(dp[s], dp[s^p]+1)
                p = (p-1)&s 
        return dp[-1]
# class Solution2:
#     def minSessions(self, tasks: List[int], sessionTime: int) -> int:
#         def canFinish(i):
#             if i == len(tasks):
#                 return True
#             for j in range(mid):
#                 if remainTime[j] >= tasks[i]:
#                     remainTime[j] -= tasks[i]
#                     if canFinish(i + 1):
#                         return True
#                     remainTime[j] += tasks[i]
#                     if remainTime[j] == sessionTime:
#                         break
#             return False                    
        
#         l, r = 1, len(tasks)
#         tasks.sort(reverse=True)
#         while l < r:
#             mid = (l + r) // 2
#             remainTime = [sessionTime] * mid
#             if not canFinish(0):
#                 l = mid + 1
#             else:
#                 r = mid
#         return l

from functools import lru_cache
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()
        n = len(tasks)
        @lru_cache(None)
        def dfs(cur):
            if cur == 0:
                return 0
            delta = cur&(-cur)
            idx = 0
            while delta > (1<<idx):
                idx += 1
            sums = sessionTime-tasks[-idx-1]
            cur -= delta
            if sums == 0 or cur == 0:
                return 1+dfs(cur)
            s = cur
            res = float('inf')
            while True:
                i, t = 0, 0
                while (s>>i) > 0:
                    if (s>>i) & 1:
                        t += tasks[-i-1]
                    i += 1
                if t <= sums:
                    res = min(res, 1+dfs(cur-s))
                if s == 0:
                    break
                s = (s-1)&cur
            # print(cur,res,sums)
            return res
        return dfs((1<<n)-1)