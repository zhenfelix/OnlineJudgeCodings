
# class Solution:
#     def minJump(self, jump: List[int]) -> int:
#         q = deque()
#         q.append(0)
#         n = len(jump)
#         visited = set()
#         visited.add(0)
#         step, reach = 1, 0
#         while q:
#             m = len(q)
#             nxt_reach = reach
#             for _ in range(m):
#                 cur = q.popleft()
#                 nxt = cur + jump[cur]
#                 # tmp.append(nxt)
#                 if nxt >= n:
#                     return step
#                 if nxt > reach and nxt not in visited:
#                     visited.add(nxt)
#                     q.append(nxt)
#                     nxt_reach = max(nxt_reach, nxt)
#                 nxt = cur - 1
#                 while nxt >= 0 and nxt not in visited:
#                     visited.add(nxt)
#                     q.append(nxt)
#                     nxt -= 1
#             reach = nxt_reach
#             step += 1
#         return step

class Solution:
    def minJump(self, jump: List[int]) -> int:
        res = n = len(jump)
        f = [n]*(n+1)
        f[0] = 0
        max_dis = [0]*(n+1) 
        curr_min_num = 0
        for i in range(0,n):
            if i>max_dis[curr_min_num]:
                curr_min_num += 1
            f[i] = min(f[i],curr_min_num+1)
            
            jump_tmp = i+jump[i]
            if jump_tmp>=n:
                res = min(res,f[i]+1)
            else:
                f[jump_tmp] = min(f[jump_tmp],f[i]+1)
                max_dis[f[i]+1] = max(max_dis[f[i]+1],jump_tmp)
        return res

# class Solution:
#     def minJump(self, jump: List[int]) -> int:
#         n = len(jump)
#         dp = [1]*n
#         for i in range(n-1)[::-1]:
#             if i+jump[i] < n:
#                 dp[i] = dp[i+jump[i]]+1
#             for j in range(i+1,n):
#                 if dp[j] <= dp[i]:
#                     break
#                 dp[j] = dp[i]+1
#         return dp[0]
