# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         cur = 1
#         while True:
#             if cur not in arr:
#                 k -= 1
#             if k <= 0:
#                 break
#             cur += 1
#         return cur

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] < mid+1+k:
                left = mid + 1
            else:
                right = mid - 1
        return right+1+k 