# class Solution:
#     def maxJumps(self, arr: List[int], d: int) -> int:
#         n = len(arr)
#         dp = [1] * (n + 1)
#         st = []
#         for i, h in enumerate(arr + [float('inf')]):
#             pre, jump = -1, 0
#             while st and arr[st[-1]] < h:
#                 cur = st.pop()
#                 if pre >= 0 and arr[cur] > arr[pre] and pre-cur <= d:
#                     dp[cur] = max(dp[cur], 1 + jump) ###buggy `pre-cur <= d` loose conditions for updating left dp values, value `jump` could come from the place out of reach for `cur` 
#                 pre = cur
#                 jump = max(jump, dp[cur])
#                 if i - cur <= d:
#                     dp[i] = max(dp[i], 1 + jump)
#             st.append(i)
#             # print(st,dp)
#         return max(dp[:-1])


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        arr += [float('inf')]
        dp = [1] * (len(arr))
        st = []
        for i, h in enumerate(arr):
            while st and arr[st[-1]] < h:
                plateau = [st.pop()]
                while st and arr[st[-1]] == arr[plateau[0]] :
                    plateau.append(st.pop())
                for p in plateau:
                    if i-p <= d:
                        dp[i] = max(dp[i], dp[p]+1)
                    if st and p-st[-1] <= d:
                        dp[st[-1]] = max(dp[st[-1]], dp[p]+1)
            st.append(i)
            # print(st,dp)
        return max(dp[:-1])


import functools

class Solution:
    def maxJumps(self, A, d):
        N = len(A)
        graph = collections.defaultdict(list)
        
        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and A[stack[-1]] < A[i]:
                    j = stack.pop()
                    if abs(i - j) <= d: graph[j].append(i)
                stack.append(i)
        
        jump(range(N))
        jump(reversed(range(N)))
        
        @functools.lru_cache(maxsize=None)
        def height(i):
            return 1 + max(map(height, graph[i]), default=0)
        
        return max(map(height, range(N)))