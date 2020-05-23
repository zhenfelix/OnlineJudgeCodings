# import bisect
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return bisect.bisect_right(nums,target)-bisect.bisect_left(nums,target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect_left(i,j):
            while i <= j:
                mid = (i+j)//2
                if nums[mid] >= target:
                    j = mid-1
                else:
                    i = mid+1
            return i
        def bisect_right(i,j):
            while i <= j:
                mid = (i+j)//2
                if nums[mid] > target:
                    j = mid-1
                else:
                    i = mid+1
            return i 
        n = len(nums)
        return bisect_right(0,n-1)-bisect_left(0,n-1)
                    
