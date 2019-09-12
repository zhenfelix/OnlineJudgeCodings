# class Solution:
#     def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
#         dp = {-1: 0}
#         arr2.sort()
        
#         def lower_bound(nums, target):
#             left, right = 0, len(nums)-1
#             while left <= right:
#                 mid = (left+right)//2
#                 if nums[mid] <= target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return left
        
#         for a in arr1:
#             tmp = collections.defaultdict(lambda: float('inf'))
#             for key in dp:
#                 if a > key:
#                     tmp[a] = min(tmp[a], dp[key])
#                 idx = lower_bound(arr2, key)
#                 if idx < len(arr2):
#                     tmp[arr2[idx]] = min(tmp[arr2[idx]], dp[key]+1)
#             dp = tmp
#         if dp:
#             return min(dp.values())
#         return -1

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(list(set(arr2)))
        arr1 = [-float('inf')] + arr1 + [float('inf')]
        n = len(arr1)
        dp = [float('inf')]*n
        
        def lower_bound(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def upper_bound(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        
        dp[0] = 0
        for i in range(1,n):
            hi = upper_bound(arr2, arr1[i])
            for j in range(i):
                if arr1[j] < arr1[i]:
                    lo = lower_bound(arr2, arr1[j])
                    if hi-lo+1 >= i-j-1:
                        dp[i] = min(dp[i], dp[j]+i-j-1)#dp[i] number of operations strictly increasing without changing arr1[i]
        print(dp)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

# https://leetcode-cn.com/circle/article/lwbQfe/
# 5184. 使数组严格递增