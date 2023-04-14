class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        n = len(nums)
        def check(x):
            if x == 1: return False
            f = 2
            while f*f <= x:
                if x%f == 0:
                    return False
                f += 1 
            return True  
        for i in range(n):
            if check(nums[i][i]):
                ans = max(ans, nums[i][i])
            if check(nums[n-1-i][i]):
                ans = max(ans, nums[n-1-i][i])
        return ans 