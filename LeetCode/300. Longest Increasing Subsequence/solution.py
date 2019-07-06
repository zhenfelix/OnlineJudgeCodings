class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(target):
            left, right = 0, maxlen-1
            print(left,right)
            while left <= right:
                mid = (left+right)//2
                if target <= dp[mid]:
                    right = mid-1
                else:
                    left = mid+1
            return right+1
        
        
        n = len(nums)
        maxlen = 0
        dp = [0]*n
        for x in nums:
            idx = binarySearch(x)
            dp[idx] = x
            if idx == maxlen:
                maxlen += 1
        return maxlen