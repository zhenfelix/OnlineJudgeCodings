# class Solution:
#     def shortestSubarray(self, A: List[int], K: int) -> int:
#         sums, res = 0, float('inf')
#         st = [(0,-1)]
#         for i, a in enumerate(A):
#             sums += a 
#             idx = bisect.bisect_right(st,(sums-K,float('inf'))) - 1
#             if idx >= 0:
#                 presum, j = st[idx]
#                 res = min(res,i-j)
#             while st and st[-1][0] >= sums:
#                 st.pop()
#             st.append((sums,i))
#         return res if res < float('inf') else -1


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        sums, res = 0, float('inf')
        q = deque([(0,-1)])
        for i, a in enumerate(A):
            sums += a 
            while q and sums - q[0][0] >= K:
                presum, j = q.popleft()
                res = min(res,i-j)
            while q and q[-1][0] >= sums:
                q.pop()
            q.append((sums,i))
        return res if res < float('inf') else -1