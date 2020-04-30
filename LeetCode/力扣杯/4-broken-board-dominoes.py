class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        brk = set()
        for b in broken:
            brk.add((b[0],b[1]))
        dp = [-1]*(1<<(m+1))
        block = (1<<(m+1))-1
        dp[(1<<(m+1))-1] = 0
        for i in range(n):
            next_dp = [-1]*(1<<(m+1))
            for state in range(1<<(m+1)):
                if block & state != block or dp[state] == -1:
                    continue
                next_dp[(state>>1)|(1<<m)] = max(next_dp[(state>>1)|(1<<m)], dp[state])
            block = (block>>1) | (1<<m)
            dp = next_dp

            for j in range(m):
                next_dp = [-1]*(1<<(m+1))
                next_block = block>>1
                for state in range(1<<(m+1)):
                    if block & state != block or dp[state] == -1:
                        continue
                    if (i,j) in brk:
                        next_dp[(state>>1)|(1<<m)] = max(next_dp[(state>>1)|(1<<m)], dp[state])
                        next_block = next_block | (1<<m)
                    else:
                        next_dp[state>>1] = max(next_dp[state>>1], dp[state])
                        if state & 1 == 0:
                            next_dp[(state>>1)|(1<<m)] = max(next_dp[(state>>1)|(1<<m)], dp[state]+1)
                        if state & (1<<m) == 0:
                            next_dp[(state>>1)|(1<<m)|(1<<(m-1))] = max(next_dp[(state>>1)|(1<<m)|(1<<(m-1))], dp[state]+1)
                dp = next_dp
                block = next_block
        return max(dp)


# from collections import defaultdict

# class Solution:
#     def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
#         def dfs(cur, visited, match):
#             for nxt in edges[cur]:
#                 if nxt not in visited:
#                     visited.add(nxt)
#                     if match.get(nxt,-1) == -1 or dfs(match[nxt],visited,match):
#                         match[cur] = nxt
#                         match[nxt] = cur
#                         return True
#             return False

#         def hungarian():
#             ans = 0
#             match = {}
#             for i in range(n):
#                 for j in range(m):
#                     cur = i*m + j
#                     if (i,j) not in brk and (i+j) & 1 and match.get(cur,-1) == -1:
#                         visited = set()
#                         # visited.add(cur)
#                         if dfs(cur, visited, match):
#                             ans += 1
#             return ans

#         edges = defaultdict(list)
#         brk = set()
#         for b in broken:
#             brk.add((b[0],b[1]))
#         for i in range(n):
#             for j in range(m):
#                 if (i,j) in brk:
#                     continue
#                 cur = i*m + j
#                 if j+1 < m and (i,j+1) not in brk:
#                     nxt = cur + 1
#                     edges[cur].append(nxt)
#                     edges[nxt].append(cur)
#                 if i+1 < n and (i+1,j) not in brk:
#                     nxt = cur + m
#                     edges[cur].append(nxt)
#                     edges[nxt].append(cur)
#         # print(edges)
#         return hungarian()