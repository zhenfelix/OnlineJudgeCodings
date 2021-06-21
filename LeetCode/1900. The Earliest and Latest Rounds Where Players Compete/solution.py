class Solution:
    def earliestAndLatest(self, n, F, S):
        ans = set()
        def dfs(pos, i):
            M, pairs = len(pos), []
            if M < 2: return

            for j in range(M//2):
                a, b = pos[j], pos[-1-j]
                if (a, b) == (F, S):
                    ans.add(i)
                    return
                if a != F and b != F and a != S and b != S:
                    pairs.append((a, b))

            addon = (F, S) if M%2 == 0 else tuple(set([F, S, pos[M//2]]))
            for elem in product(*pairs):
                dfs(sorted(elem + addon), i + 1)

        dfs(list(range(1, n+1)), 1)
        return [min(ans), max(ans)]


# class Solution:
#     def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
#         res = [n, 0]
#         def dfs(cur, nxt, left, right, level):
#             if left > right:
#                 dfs(sorted(nxt), [], 0, len(nxt)-1, level+1)
#                 return
#             elif left == right:
#                 dfs(cur, nxt+[cur[left]], left+1, right-1, level)
#                 return

#             if (cur[left] == firstPlayer and cur[right] == secondPlayer) or (cur[left] == secondPlayer and cur[right] == firstPlayer):
#                 res[0] = min(res[0], level)
#                 res[1] = max(res[1], level)
#             elif cur[left] == firstPlayer or cur[left] == secondPlayer:
#                 dfs(cur, nxt+[cur[left]], left+1, right-1, level)
#             elif cur[right] == firstPlayer or cur[right] == secondPlayer:
#                 dfs(cur, nxt+[cur[right]], left+1, right-1, level)
#             else:
#                 dfs(cur, nxt+[cur[left]], left+1, right-1, level)
#                 dfs(cur, nxt+[cur[right]], left+1, right-1, level)
#             return

#         dfs([i+1 for i in range(n)], [], 0, n-1, 1)
#         return res


class Solution:
    def earliestAndLatest(self, n, F, S):
        @lru_cache(None)
        def dp(l, r, m, q):
            # print(l,r,m,q)
            if l > r:  dp(r, l, m, q)
            if l == r: ans.add(q)
            delta = 0
            if r > (m+1)//2: 
                delta = r-(m+2)//2
                r = m+1-r
            for i in range(1, l + 1):
                for j in range(l-i+1, r-i+1):
                    dp(i, j+delta, (m + 1) // 2, q + 1)
                    
                            
        ans = set()
        F, S = min(F,S), max(F,S)
        dp(F, n-S+1, n, 1)
        return [min(ans), max(ans)]

