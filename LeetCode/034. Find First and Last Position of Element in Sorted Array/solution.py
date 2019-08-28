class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def beforeK(nums, left, right, t):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < t:
                    left = mid+1
                else:
                    right = mid-1
            return left
        
        def afterK(nums, left, right, t):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > t:
                    right = mid-1
                else:
                    left = mid+1
            return right
        
        a, b = beforeK(nums,0,len(nums)-1,target), afterK(nums,0,len(nums)-1,target)
        if a > b:
            return [-1,-1]
        return [a,b]

