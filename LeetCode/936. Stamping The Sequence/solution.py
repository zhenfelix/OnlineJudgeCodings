class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        sz = n-m+1
        degree = [0]*sz
        edges = [[] for _ in range(n)]
        mismatch = [True]*n 
        for i in range(sz):
            for j in range(m):
                if stamp[j] != target[i+j]:
                    degree[i] += 1
                    edges[i+j].append(i)
        q = deque()
        ans = []
        for i in range(sz):
            if degree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for j in range(m):
                if mismatch[cur+j]:
                    mismatch[cur+j] = False
                    for nxt in edges[cur+j]:
                        degree[nxt] -= 1
                        if degree[nxt] == 0:
                            q.append(nxt)
        if len(ans) == sz:
            return ans[::-1]
        return []


    def movesToStamp(self, s, t):
        n, m, t, s, res = len(t), len(s), list(t), list(s), []

        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?': continue
                if t[i + j] != s[j]: return False
                changed = True
            if changed:
                t[i:i + m] = ['?'] * m
                res.append(i)
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)
        return res[::-1] if t == ['?'] * n else []


# class Solution:
#     def movesToStamp(self, s, t):
#         if s[0] != t[0] or s[-1] != t[-1]: return []
#         n, m = len(s), len(t)
#         path = [0] * m
#         pos = collections.defaultdict(set)
#         for i, c in enumerate(s): pos[c].add(i)

#         def dfs(i, index):
#             path[i] = index
#             if i == m - 1: return index == n - 1
#             nxt_index = set()
#             if index == n - 1:  # rule 2
#                 nxt_index |= pos[t[i + 1]]
#             if index < n - 1 and s[index + 1] == t[i + 1]:  # rule 0
#                 nxt_index.add(index + 1)
#             if s[0] == t[i + 1]:  # rule 1
#                 nxt_index.add(0)
#             return any(dfs(i + 1, j) for j in nxt_index)

#         def path2res(path):
#             down, up = [], []
#             for i in range(len(path)):
#                 if path[i] == 0:
#                     up.append(i)
#                 elif i and path[i] - 1 != path[i - 1]:
#                     down.append(i - path[i])
#             return down[::-1] + up

#         if not dfs(0, 0): return []
#         return path2res(path)        