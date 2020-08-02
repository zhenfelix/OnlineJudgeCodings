class Solution:
    def getWinner(self, A, k):
        cur = A[0]
        win = 0
        for i in range(1, len(A)):
            if A[i] > cur:
                cur = A[i]
                win = 0
            win += 1
            if (win == k): break
        return cur        

# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:
#         q, n, cnt = deque(arr), len(arr), 0
#         candidate = q.popleft()
#         while True:
#             cur = q.popleft()
#             if candidate > cur:
#                 cnt += 1
#                 q.append(cur)
#             else:
#                 cnt = 1
#                 q.append(candidate)
#                 candidate = cur
#             if cnt >= k or cnt >= n:
#                 return candidate
#         return -1