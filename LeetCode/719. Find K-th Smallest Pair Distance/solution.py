# from collections import defaultdict

# class Solution:
#     def smallestDistancePair(self, nums: List[int], k: int) -> int:
#         nums = sorted(nums)
#         maxn = nums[-1]+1
#         cc = defaultdict(int)
#         idx = {}
#         precc = [0]*maxn
#         cur = 0
#         for i, num in enumerate(nums):
#             cc[num] += 1
#             if num not in idx:
#                 idx[num] = i
#         for num in range(maxn) :
#             if num > 0:
#                 precc[num] += precc[num-1]
#             precc[num] += cc[num]
        
#         # print(precc)
#         # print(cc)
#         # print(idx)
#         def get_count(value):
#             res = 0
#             for i, num in enumerate(nums):
#                 hi, low = num + value, num
#                 if hi > maxn-1:
#                     hi = maxn-1
#                 res += precc[hi] - precc[low] - i + idx[low] + cc[low] - 1
#                 # print(res)
            
#             return res
        
#         left, right = 0, maxn-1
#         while left <= right:
#             mid = (left+right)//2
#             res = get_count(mid)
#             if res >= k:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return left
                

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def isPossible(v):
            res, left, right = 0, 0, 0
            for right, x in enumerate(nums):
                while nums[right] - nums[left] > v:
                    left += 1
                res += right - left
            return res >= k
            
        nums = sorted(nums)
        lo, hi = 0, nums[-1]-nums[0]
        while lo <= hi:
            mid = (lo+hi)//2
            if isPossible(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo
            