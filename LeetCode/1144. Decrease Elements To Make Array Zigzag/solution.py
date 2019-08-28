class Solution:
#     def movesToMakeZigzag(self, nums: List[int]) -> int:
#         a1, a2 = 0, 0
#         n = len(nums)
#         arr = nums.copy()
#         for i, a in enumerate(arr):
#             if i+1 < n:
#                 if i%2 == 0:
#                     if arr[i] <= arr[i+1]:
#                         a1 += arr[i+1]-arr[i]+1
#                         arr[i+1] = arr[i]-1
#                 else:
#                     if arr[i] >= arr[i+1]:
#                         a1 += arr[i]-arr[i+1]+1
#                         arr[i] = arr[i+1]-1
        
#         arr = nums.copy()
#         for i, a in enumerate(arr):
#             if i+1 < n:
#                 if i%2 == 0:
#                     if arr[i] >= arr[i+1]:
#                         a2 += arr[i]-arr[i+1]+1
#                         arr[i] = arr[i+1]-1
#                 else:
#                     if arr[i] <= arr[i+1]:
#                         a2 += arr[i+1]-arr[i]+1
#                         arr[i+1] = arr[i]-1
#         return min(a1, a2)

    def movesToMakeZigzag(self, A):
        A = [float('inf')] + A + [float('inf')]
        res = [0, 0]
        for i in range(1, len(A) - 1):
            res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
        return min(res)