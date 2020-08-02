# class Solution(object):
#     def pyramidTransition(self, bottom, allowed):
#         T = collections.defaultdict(set)
#         for u, v, w in allowed:
#             T[u, v].add(w)

#         #Comments can be used to cache intermediate results
#         #seen = set()
#         def solve(A):
#             if len(A) == 1: return True
#             #if A in seen: return False
#             #seen.add(A)
#             return any(solve(cand) for cand in build(A, []))

#         def build(A, ans, i = 0):
#             if i + 1 == len(A):
#                 yield "".join(ans)
#             else:
#                 for w in T[A[i], A[i+1]]:
#                     ans.append(w)
#                     for result in build(A, ans, i+1):
#                         yield result
#                     ans.pop()

#         return solve(bottom)


# class Solution:
#     def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
#         allowed = set(allowed)
#         mp = "ABCDEFG"
#         def dfs(cur):
#             n = len(cur)
#             if n <= 1:
#                 return True
#             arrs = []

#             def dfs2(st):
#                 m = len(st)
#                 if m == n-1:
#                     arrs.append(st)
#                     return
#                 for ch in mp:
#                     if cur[m]+cur[m+1]+ch in allowed:
#                         dfs2(st+ch)
#                 return
            
#             dfs2('')
#             for nxt in arrs:
#                 if dfs(nxt):
#                     return True
#             return False

#         return dfs(bottom)


class Solution(object):

    def pyramidTransition(self, bottom, allowed):
        f = collections.defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1: return True
            for i in itertools.product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i): return True
            return False
        return pyramid(bottom)