# from collections import deque

# class Solution(object):
#     def shortestSuperstring(self, A):
#         """
#         :type A: List[str]
#         :rtype: str
#         """
#         n = len(A)
#         graph = [[0]*n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 for k in range(min(len(A[i]),len(A[j]))-1,-1,-1):

#                     if A[i][-k:] == A[j][:k]:
#                         # print(A[i][-k:])
#                         # print(A[j][:k])
#                         graph[i][j] = -k
#                         break
#         # print(graph)
#         q = deque()
#         dp = {}
#         for i in range(n):
#             dp[i,i,A[i],1] = 0
#             q.append((i,i,A[i],1))
#         ans_len, ans_path = float('inf'), ""
#         while q:
#             start, end, path, cnt = q.popleft()
#             if cnt == n:
#                 if dp[start,end,path,cnt] < ans_len:
#                     ans_len = dp[start,end,path,cnt]
#                     ans_path = path 
#                 continue
#             for nxt in range(n):
#                 if A[nxt] not in path:
#                     dp[start,nxt,path+A[nxt][-graph[end][nxt]:],cnt+1] = dp[start,end,path,cnt] + graph[end][nxt]
#                     q.append((start,nxt,path+A[nxt][-graph[end][nxt]:],cnt+1))


#         return ans_path


# from collections import deque

# class Solution(object):
#     def shortestSuperstring(self, A):
#         """
#         :type A: List[str]
#         :rtype: str
#         """
#         n = len(A)
#         graph = [[0]*n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 for k in range(min(len(A[i]),len(A[j]))-1,-1,-1):

#                     if A[i][-k:] == A[j][:k]:
#                         # print(A[i][-k:])
#                         # print(A[j][:k])
#                         graph[i][j] = -k
#                         break
#         # print(graph)
#         q = deque()
#         dp = {}
#         for i in range(n):
#             dp[i,i,1<<i] = 0
#             q.append((i,i,1<<i))
#         parent = {}
#         while q:
#             start, end, state = q.popleft()
#             # if cnt == n:
#             #     if dp[start,end,path,cnt] < ans_len:
#             #         ans_len = dp[start,end,path,cnt]
#             #         ans_path = path 
#             #     continue
#             # if state == (1<<n)-1:
#             #     continue
#             for nxt in range(n):
#                 if state & (1<<nxt) == 0:
#                     if (start,nxt,state | (1<<nxt)) not in dp and (state | (1<<nxt)) != (1<<n)-1:
#                         q.append((start,nxt,state | (1<<nxt)))
#                     if (start,nxt,state | (1<<nxt)) not in dp or dp[start,end,state] + graph[end][nxt] < dp[start,nxt,state | (1<<nxt)]:
#                         dp[start,nxt,state | (1<<nxt)] = dp[start,end,state] + graph[end][nxt]
#                         parent[start,nxt,state | (1<<nxt)] = end

#         # print(parent)
#         end_candidate = []
#         for start in range(n):
#             end_candidate.append(min(list(range(n)), key = lambda x: dp.get((start,x,(1<<n)-1),float('inf'))))
#         start = min(list(range(n)), key = lambda x: dp.get((x,end_candidate[x],(1<<n)-1),float('inf')))
#         end = end_candidate[start]
#         cur, state = end, (1<<n)-1
#         path = []
#         for i in range(n-1,-1,-1):
#             path.append(cur)
#             cur = parent.get((start,cur,state),-1)
#             state = state - (1<<path[-1])
#         path = path[::-1]
#         # print(path)
#         ans = A[path[0]]
#         for i in range(1,n):
#             ans += A[path[i]][-graph[path[i-1]][path[i]]:]

#         return ans


from collections import deque

class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        n = len(A)
        graph = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(min(len(A[i]),len(A[j]))-1,-1,-1):

                    if A[i][-k:] == A[j][:k]:
                        # print(A[i][-k:])
                        # print(A[j][:k])
                        graph[i][j] = -k
                        break
        # print(graph)
        q = deque()
        dp = {}
        for i in range(n):
            dp[i,1<<i] = 0
            q.append((i,1<<i))
        parent = {}
        while q:
            end, state = q.popleft()
            for nxt in range(n):
                if state & (1<<nxt) == 0:
                    if (nxt,state | (1<<nxt)) not in dp:
                    # if (nxt,state | (1<<nxt)) not in dp and (state | (1<<nxt)) != (1<<n)-1:
                        q.append((nxt,state | (1<<nxt)))
                    if (nxt,state | (1<<nxt)) not in dp or dp[end,state] + graph[end][nxt] < dp[nxt,state | (1<<nxt)]:
                        dp[nxt,state | (1<<nxt)] = dp[end,state] + graph[end][nxt]
                        parent[nxt,state | (1<<nxt)] = end

        # print(parent)
        end = min(list(range(n)), key = lambda x: dp.get((x,(1<<n)-1),float('inf')))
        
        cur, state = end, (1<<n)-1
        path = []
        for i in range(n-1,-1,-1):
            path.append(cur)
            cur = parent.get((cur,state),-1)
            state = state - (1<<path[-1])
        path = path[::-1]
        # print(path)
        ans = A[path[0]]
        for i in range(1,n):
            ans += A[path[i]][-graph[path[i-1]][path[i]]:]

        return ans


import functools
class Solution:
    def graphGen(self, A):
        n, Mod = len(A), 10**9+7
        graph = [[0]*n for _ in range(n)]
        suffix = defaultdict(list)
        for i, a in enumerate(A):
            cur = 0
            for j in range(len(a)):
                cur += ord(a[-j-1])*256**j
                cur %= Mod
                suffix[cur].append(i)
        for i, a in enumerate(A):
            cur = 0
            for j in range(len(a)):
                cur = cur*256+ord(a[j])
                cur %= Mod
                for pre in suffix[cur]:
                    if pre == i:
                        continue
                    graph[pre][i] = -j-1
        return graph



    def shortestSuperstring(self, A: List[str]) -> str:
        A.append('')
        n = len(A)
        graph = self.graphGen(A)
        dp = {}
        for i in range(n):
            dp[i,1<<i] = i 
        @functools.lru_cache(None)
        def dfs(i,state):
            if state == (1<<i):
                return len(A[i])
            res = float('inf')
            for j in range(n):
                if j == i or state & (1<<j) == 0:
                    continue
                if res > dfs(j,state^(1<<i))+graph[j][i]:
                    res = dfs(j,state^(1<<i))+graph[j][i]
                    dp[i,state] = j
            return res+len(A[i])
        dfs(n-1,(1<<n)-1)
        start, ans = (n-1,(1<<n)-1), []
        while dp[start] != start[0]:
            state_ = start[-1]
            idx = dp[start]
            state_ ^= (1<<start[0])
            start = (idx, state_)
            ans.append(A[idx][-graph[dp[start]][idx]:])
        return ''.join(ans[::-1])