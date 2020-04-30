# class Solution:
#     def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
#         g = defaultdict(list)
#         for a, b in relation:
#             g[a].append(b)
#         path = [0]*n 
#         path[0] = 1
#         for _ in range(k):
#             tmp = [0]*n 
#             for cur in range(n):
#                 for nxt in g[cur]:
#                     tmp[nxt] += path[cur]
#             path = tmp
#         return path[-1]

class Solution:
    def numWays(self, n: int, relation: List[int], k: int) -> int:
        dp = [0]*n 
        dp[0] = 1

        for t in range(0,k):
            nxt = [0]*n 
            for x,y in relation:
                nxt[y] += dp[x]
            dp = nxt
        return dp[-1]


