class Solution:
    def mostVisited(self, n, A):
        return list(range(A[0], A[-1] + 1)) or list(range(1, A[-1] + 1)) + list(range(A[0], n + 1))        


# class Solution:
#     def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
#         cnt = [0]*(n+1)
#         rounds = deque(rounds)
#         cur = rounds.popleft()
#         while rounds:
#             cnt[cur] += 1
#             if cur == rounds[0]:
#                 rounds.popleft()
#             cur += 1
#             if cur > n: cur = 1

#         return [i for i in range(1,n+1) if cnt[i] == max(cnt)]