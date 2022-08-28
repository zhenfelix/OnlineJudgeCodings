# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         n = len(arr)
#         left, right = 0, n-1
#         while left <= right:
#             mid = (left + right)// 2
#             if arr[mid] <= x:
#                 left = mid + 1
#             else:
#                 right = mid - 1
                
#         left, right = right, left
#         while k:
#             if right > n-1 or (left >= 0 and x-arr[left] <= arr[right]-x):
#                 left -= 1
#             else:
#                 right += 1
#             k -= 1
#         return arr[left+1:right]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-1-k
        while left <= right:
            mid = (left+right)//2
            # print(mid, arr[mid])
            # if abs(x-arr[mid]) <= abs(arr[mid+k]-x):
            if x-arr[mid] <= arr[mid+k]-x:
                right = mid - 1
            else:
                left = mid + 1
        return arr[left:left+k]


# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         nums = [(abs(y-x),y) for y in arr]
#         nums = sorted(nums)[:k]
#         return [y for _, y in sorted(nums, key = lambda t: t[-1])]